from django.urls import path, re_path

from index.views import *

app_name = 'index'

urlpatterns = [
    path('about/', about, name='about'),
    path('', home , name='home'),
    path('team/', team, name='team'),
    path('subscribe/', subscribe, name='subscribe'),
]