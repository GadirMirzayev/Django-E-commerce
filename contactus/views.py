from django.shortcuts import render, redirect
from django.contrib import messages
from index.forms import SubscriberForm 
from contactus.models import *
from contactus.forms import *
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
)

# Create your views here.

class ContactView(CreateView):
    form_class = ContactForm
    #fields = '__all__'
    #model = Contact
    template_name = 'contact.html'
    success_url = reverse_lazy('home:home')

    def form_valid(self, form):
        result = super(ContactView, self).form_valid(form)
        messages.success(self.request, 'Mesajiniz gonderildi. Sizinle yaxinda elaqe saxlanilacaq!')
        return result