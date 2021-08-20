from django.contrib import admin
from checkout.models import (
   Checkout,
   Wishlist,
   BasketItem,
)
# Register your models here.
@admin.register(Checkout)
class CheckoutsAdmin(admin.ModelAdmin):
    list_filter = ('first_name',)
    search_fields = ('first_name',)


admin.site.register(Wishlist)
admin.site.register(BasketItem)