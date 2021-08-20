from django.urls import path, re_path

from product.views import *

app_name = 'product'

urlpatterns = [
    path('customer-review/', customer_review, name='customer_review'),
    path('product-details/<int:pk>/', ProductDetailView.as_view(), name="product_detail"),
    path('shop/', ProductListView.as_view(), name='shop'),
]