from django.template import Library
from accounts.forms import LoginForm, RegistrationForm

register = Library()


@register.simple_tag
def get_login():
    return LoginForm


@register.simple_tag
def get_register():
    return RegistrationForm