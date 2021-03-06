"""code_for_good URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='Pastebin API')

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('schema', schema_view),
    path('invite-partner', views.invite, name='send_invite'),
    path('register', views.register, name='register'),
    path('review', views.review, name='review_partner'),
    path('approve-partner', views.approve, name='approve'),
]
