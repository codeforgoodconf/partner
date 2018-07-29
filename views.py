import json

from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.http import JsonResponse
from django.shortcuts import render
from django.template.loader import get_template, render_to_string
from django.views.decorators.csrf import csrf_exempt

from .models import Partner, PARTNER_APPROVED


# Create your views here.


def index(request):
    context = {}
    return render(request, 'partner/index.html', context)


@csrf_exempt
def invite(request):
    data = json.loads(request.body)
    partner_json = data.get('partner', '') # FIXME: validate json

    partner, created = Partner.objects.get_or_create(
        id=partner_json['partner_id'],
        diaper_bank_id=partner_json['diaper_bank_id'],
    )

    if created:
        # new partner, make them a user
        partner.user = User.objects.create(
            username=partner_json['email']
        )

    if partner.email != partner_json['email']:
        # if new partner, or if invite was sent to existing partner with a different email, update the email
        partner.email = partner_json['email']
        partner.save()

    context = {'partner_id': partner.id}
    html_content = get_template('partner/invite_partner.html').render(context)
    plaintext_content = render_to_string('partner/invite_partner.txt', context)
    send_mail('Diaper bank partner registration', plaintext_content, 'diaperbankpartners@gmail.com', [partner.email], fail_silently=False, html_message=html_content)
    return JsonResponse({'status': 'ok'})


def register(request):
    # FIXME actual form page here
    id = request.GET.get('id', '') # FIXME: what should we return if there's no id?

    partner = Partner.objects.get(id=id)
    context = {
        'id': partner.id,
        'diaper_bank_id': partner.diaper_bank_id,
        'email': partner.email,
        'status': partner.status,
    }
    return render(request, 'partner/register.html', context)


@csrf_exempt
def review(request):
    req_data = json.loads(request.body).get('partner', '')
    partner = Partner.objects.get(id=req_data['partner_id']).__dict__
    del partner['_state']
    del partner['user_id']
    partner['partner_id'] = partner['id']
    return JsonResponse(partner)


@csrf_exempt
def approve(request):
    data = json.loads(request.body)
    partner_json = data.get('partner', '') # FIXME: validate json
    partner = Partner.objects.get(id=partner_json['partner_id'])
    partner.status = PARTNER_APPROVED
    partner.save()
    return JsonResponse({'status': 'ok'})
