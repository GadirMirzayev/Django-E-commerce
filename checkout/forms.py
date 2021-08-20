from django import forms
from checkout.models import *


class CheckoutForm(forms.ModelForm):
    class Meta:
        model = Checkout
        fields = (
            'first_name',
            'last_name',
            'email',
            'phone',
            'message',
            'country',
            'company_name',
            'state',
            'zip_code',
            'name_on_card',
            'card_number',
            'date',
            'security_code',
        )
        widgets = {
            'first_name': forms.TextInput(attrs={
                'placeholder': 'First Name'
            }),
            'last_name': forms.TextInput(attrs={
                'placeholder': 'Last Name'
            }),
            'email': forms.EmailInput(attrs={
                'placeholder': 'Email'
            }),
            'phone': forms.TextInput(attrs={
                'placeholder': 'Phone'
            }),
            'message': forms.Textarea(attrs={
                'placeholder': 'Message'
            }),
            'country': forms.Select(attrs={
            }),
            'company_name': forms.TextInput(attrs={
                'placeholder': 'Company Name'
            }),
            'state': forms.TextInput(attrs={
                'placeholder': 'State'
            }),
            'zip_code': forms.TextInput(attrs={
                'placeholder': 'Zip Code'
            }),
            'name_on_card': forms.TextInput(attrs={
                'placeholder': 'Name on Card'
            }),
            'card_number': forms.TextInput(attrs={
                'placeholder': 'Card Number'
            }),
            'date': forms.DateInput(attrs={
                'placeholder': 'Date'
            }),
            'security_code': forms.TextInput(attrs={
                'placeholder': 'Security Code'
            }),
        }

