from django.urls import path
from checkout.api.views import BasketItemListView, BasketItemDetailView

app_name = 'api'

urlpatterns = [
    path('ordered-items/', BasketItemListView.as_view(), name='ordered_items_api'),
    path('ordered-items/<int:pk>/', BasketItemDetailView.as_view(), name='checkout_detail_api'),
]