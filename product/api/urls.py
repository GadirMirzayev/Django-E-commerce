from django.urls import path
from product.api.views import products, product_categories, product_detail, product_category_detail


urlpatterns = [
    path('products/', products, name='products_api'),
    path('product_categories/', product_categories, name='categories_api'),
    path('products/<int:pk>', product_detail, name='products_detail_api'),
    path('product_categories/<int:pk>', product_category_detail, name='categories_detail_api'),
]