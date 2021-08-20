from django.urls import path, re_path

from contactus.views import *

app_name = 'contactus'

urlpatterns = [
    path('contact/', ContactView.as_view(), name='contact'),
]