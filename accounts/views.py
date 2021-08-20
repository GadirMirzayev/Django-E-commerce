from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib import messages
from django.utils.encoding import force_text
from django.utils.http import urlsafe_base64_decode
from django.contrib.auth import  get_user_model
from django.contrib.auth import authenticate, login as django_login, logout as django_logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.views.generic import (
    CreateView, TemplateView
)

# Create your views here.
from accounts.forms import RegistrationForm, LoginForm , PasswordChangeForm
from accounts.tasks import send_confirmation_mail
from accounts.tools.tokens import account_activation_token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from accounts.serializers import UserLoginSerializer
from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework.views import APIView

User = get_user_model()


class CustomAuthToken(APIView):

    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return Response({
            'success': False,
            'message': "You are already authenticated",
            }, status=400)
        data = request.data
        username = data.get('username', False)
        password = data.get('password', False)
        if username and password:
            user = authenticate(username=username, password=password, )
            if user:
                django_login(request, user)
                token, _ = Token.objects.get_or_create(user=user)
                serializer = UserLoginSerializer(user)
                return Response({
                    'id': user.id,
                    'success': True,
                    'message': "Success",
                    'token': token.key,
                    "data": serializer.data
                }, status=200)
        return Response({
            'success': False,
            'message': "Invalid credentials",
        }, status=401)



class RegisterView(CreateView):
    template_name = 'registration/login.html'
    form_class = RegistrationForm
    success_url = reverse_lazy('index:home')

    def form_valid(self, form):
        result = super(RegisterView, self).form_valid(form)
        user = form.save(commit=False)
        user.is_active = False
        user.save()
        site_address = self.request.is_secure() and "https://" or "http://" + self.request.META['HTTP_HOST']
        send_confirmation_mail(user_id=user.id, site_address=site_address)
        messages.success(self.request, 'Siz ugurla qeydiyyatdan kecdiniz')
        return result

# def register(request):
#     form = RegistrationForm()
#     if request.method == 'POST':
#         form = RegistrationForm(data=request.POST, files=request.FILES)
#         if form.is_valid():
#             user = form.save(commit=False)
#             user.is_active = False
#             user.save()
#             # http://example.com
#             site_address = request.is_secure() and "https://" or "http://" + request.META['HTTP_HOST']  # https
#             send_confirmation_mail(user_id=user.id, site_address=site_address)
#             messages.success(request, 'Siz ugurla qeydiyyatdan kecdiniz')
#             return redirect(reverse_lazy('index:home'))
#     context = {
#         'register_form': form  
#     }
#     return render(request, 'login-register.html', context)


def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        messages.success(request, 'Email is activated')
        return redirect(reverse_lazy('index:home'))
    elif user:
        messages.error(request, 'Email is not activated. May be is already activated')
        return redirect(reverse_lazy('accounts:register'))
    else:
        messages.error(request, 'Email is not activated')
        return redirect(reverse_lazy('accounts:register'))



class LoginView(TemplateView):
    template_name = 'registration/login.html'



class LogoutView(LoginRequiredMixin ,APIView):
    def get(self, request, format=None):
        django_logout(request)
        messages.success(request, 'Siz cixish etdiniz.')
        return Response({'message':"Siz cixish etdiniz."})



@login_required
def change_password(request):
    form = PasswordChangeForm()
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST)
        if form.is_valid():
            old_password = form.cleaned_data["old_password"]
            if not request.user.check_password(old_password):
                messages.error(request, 'Kohne sifre yanlishdir!')
                return redirect(reverse_lazy('accounts:change_password'))
            password1 = form.cleaned_data.get('new_password1')
            password2 = form.cleaned_data.get('new_password2')
            if password1 != password2:
                messages.error(request, 'Yeni sifreler ust-uste dushmur!')
                return redirect(reverse_lazy('accounts:change_password'))
            request.user.set_password(form.cleaned_data["new_password1"])
            request.user.save()
            return redirect(reverse_lazy('index:home'))
    context = {
        'form': form
    }
    return render(request, 'change_password.html',context)