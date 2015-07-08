__author__ = 'Alexandre Cloquet'

from django.contrib.auth.models import User
from SuperPortal.models import GuildSettings

from django import forms

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        exclude = ()

class GuildSettingsForm(forms.ModelForm):

    class Meta:
        model = GuildSettings
        exclude = ()