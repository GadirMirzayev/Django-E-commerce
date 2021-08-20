from django import forms
from contactus.models import *


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact_Info
        fields = (
            'name',
            'email',
            'subject',
            'message',
        )
        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': 'Name'
            }),
            'email': forms.EmailInput(attrs={
                'placeholder': 'Email'
            }),
            'subject': forms.TextInput(attrs={
                'placeholder': 'Subject'
            }),
            'message': forms.Textarea(attrs={
                'placeholder': 'Message'
            }),
        }
