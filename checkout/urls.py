from django.urls import path, re_path

from checkout.views import *
app_name = 'checkout'

urlpatterns = [
    path('cart/', CartView.as_view(), name='cart'),
    path('check-out/', check_out, name='checkout'),
    path('wishlist/', wishlist, name='wishlist'),
]