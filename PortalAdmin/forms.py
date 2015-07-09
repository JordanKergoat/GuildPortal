__author__ = 'Alexandre Cloquet'

from django.contrib.auth.models import User
from SuperPortal.models import GuildSettings
from PortalEnrollment.models import EnrollmentSettings

from django import forms

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        exclude = ()

class GuildSettingsForm(forms.ModelForm):

    class Meta:
        model = GuildSettings
        exclude = ()

class EnrollmentSettingsForm(forms.ModelForm):

    class Meta:
        model = EnrollmentSettings
        exclude = ('game_choice', )