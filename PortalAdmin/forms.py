__author__ = 'Alexandre Cloquet'

from django.contrib.auth.models import User
from SuperPortal.models import GuildSettings
from PortalEnrollment.models import EnrollmentSettings
from Portal.models.enrollment import TypeValue, FieldValue

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

class TableNameForm(forms.ModelForm):

    class Meta:
        model = TypeValue
        exclude = ('game', )

class DbEntryForm(forms.ModelForm):

    class Meta:
        model = FieldValue
        exclude = ()