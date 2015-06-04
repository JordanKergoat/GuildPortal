from django import forms

__author__ = 'Alexandre Cloquet'
from PortalEnrollment.models import Enrollement


class EnrollementForm(forms.ModelForm):
    # characters_choice = forms.CharField(widget=forms.Select())
    class Meta:
        model = Enrollement
        exclude = ('roles',)