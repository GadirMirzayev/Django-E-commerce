from django import forms
from index.models import *
from index.utils.validators import mail_validator
from django.core.exceptions import ValidationError

class SubscriberForm(forms.ModelForm):

    class Meta:
        model = Subscriber
        fields = (
            'email',
        )
        widgets = {
            'email': forms.EmailInput(attrs={
                'class':"email",
                'id':"mce-EMAIL",
                'placeholder': 'Email Address'
            }),
        }

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not email.endswith('gmail.com'):
            raise forms.ValidationError('Daxil edilen email yanliz gmail hesabi olmalidir')
        return email