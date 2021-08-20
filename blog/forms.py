from django import forms
from blog.models import *

class CommentForm(forms.ModelForm):

    class Meta:
        model = BlogComment
        fields = (
            'text',
            'parent_comment',
        )
        widgets = {
            'text': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Message'
                
            }),
            'parent_comment': forms.HiddenInput()

        }