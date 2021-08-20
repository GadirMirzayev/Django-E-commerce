from django.contrib import admin
from index.models import Subscriber
# Register your models here.

@admin.register(Subscriber)
class SubscriberAdmin(admin.ModelAdmin):
    list_filter = ('email',)
    search_fields = ('email',)