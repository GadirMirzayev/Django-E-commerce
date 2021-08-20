from django.shortcuts import render, redirect
from django.contrib import messages
from index.forms import SubscriberForm
from checkout.models import *
from checkout.forms import *
from django.views.generic import (
    TemplateView,
)


# Create your views here.

class CartView(TemplateView):
    template_name = 'cart.html'

# def cart(request):
#     form1 = SubscriberForm()
#     context = {
#         'form1': form1
#     }
#     return render(request, "cart.html",context)


def check_out(request):
    form = CheckoutForm()
    if request.method == 'POST':
        form = CheckoutForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Bizden Alish-Verish etdiyiniz ucun tesekkur edirik!')
            return redirect('/')
    context = {
        'form' : form
    }
    return render(request, "checkout.html",context)


def wishlist(request):
    return render(request, "wishlist.html",context)