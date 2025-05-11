from django import forms
from products.models import LogMessage
from .models import Comment

class LogMessageForm(forms.ModelForm):
    class Meta:
        model = LogMessage
        fields = ("message",) # NOTE: the trailing comma is required

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'text']