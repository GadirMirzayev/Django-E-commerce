from django.urls import path, re_path
from django.contrib.auth import views as auth_views
from accounts.views import RegisterView, activate, LoginView, LogoutView, change_password
from django.urls import reverse_lazy

app_name = 'accounts'

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    re_path(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,33})/$',
            activate, name='activate'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('change-password/', change_password, name='change_password'),
    path('reset-password/', 
        auth_views.PasswordResetView.as_view(
        template_name="reset/password_reset.html",
        success_url = reverse_lazy('accounts:password_reset_done')), 
        name='reset_password'),
    path('reset-password-done/', 
        auth_views.PasswordResetDoneView.as_view(template_name="reset/password_reset_done.html"), 
        name='password_reset_done'),
    path('reset/<uidb64>/<token>/', 
        auth_views.PasswordResetConfirmView.as_view(template_name="reset/password_reset_confirm.html"),
        name='password_reset_confirm'),
    path('reset-password-complete/', 
        auth_views.PasswordResetCompleteView.as_view(template_name="reset/password_reset_complete.html"),
        name='password_reset_complete'),
]