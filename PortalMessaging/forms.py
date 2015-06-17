__author__ = 'cloquet'

from django import forms
from .models import Message

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        exclude = ('time_send', 'time_read', 'reply', 'sender')

class ReplyForm(forms.ModelForm):
    class Meta:
        model = Message
        exclude = ('time_send', 'time_read', 'reply', 'sender', 'receiver')
