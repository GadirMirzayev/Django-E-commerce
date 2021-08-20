from django.shortcuts import render,redirect
from django.contrib import messages
from django.http import HttpResponseRedirect
from index.forms import *

# Create your views here.
def about(request):
    return render(request, "about.html",)


def home(request):
    return render(request, "index.html", )


def team(request):
    return render(request, "team.html",)


def subscribe(request):
    form1 = SubscriberForm()
    if request.method == 'POST':
        form1 = SubscriberForm(data=request.POST)
        if form1.is_valid():
            form1.save()
            messages.success(request, 'Siz abune oldunuz.')
            return redirect(request.META.get("HTTP_REFERER"))
    return redirect(request.META.get("HTTP_REFERER"))