import json

from django.core.mail import send_mail
from django.http import JsonResponse
from django.shortcuts import render
from django.template.loader import get_template, render_to_string
from django.views.decorators.csrf import csrf_exempt


# Create your views here.


def index(request):
    context = {}
    return render(request, 'partner/index.html', context)


@csrf_exempt
def send_invite(request):
    data = json.loads(request.body)
    partner = data.get('partner', '')
    # FIXME: should validate json data and send back an error if it fails validation
    # TODO: partner db object should get saved at this point, with its id, email, and diaper_bank_id fields filled out
    context = {'partner_id': partner['partner_id']}
    html_content = get_template('partner/invite_partner.html').render(context)
    plaintext_content = render_to_string('partner/invite_partner.txt', context)
    send_mail('Diaper bank partner registration', plaintext_content, 'diaperbankpartners@gmail.com', [partner['email']], fail_silently=False, html_message=html_content)
    return JsonResponse({'status': 'ok'})


def register(request):
    id = request.GET.get('id', '')
    # FIXME: what should we return if there's no id?
    # TODO: lookup partner by id and give them a form they can sumbit to their diaper bank
    context = {}
    return render(request, 'partner/register.html', context)
