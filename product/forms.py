from django import forms
from product.models import *

class ReviewForm(forms.ModelForm):

    users_rating = forms.ChoiceField( choices =Review.CHOICES, widget = forms.RadioSelect())
    class Meta:
        model = Review
        fields = (
            'text',
            'users_rating'
        )
        widgets = {
            'text': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Message'
            }),
        }