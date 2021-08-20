from django.contrib import admin
from contactus.models import Contact_Info
# Register your models here.

@admin.register(Contact_Info)
class Contact_InfoAdmin(admin.ModelAdmin):
    list_filter = ('name', 'email', 'subject','message')
    search_fields = ('name', 'email', 'subject','message')
