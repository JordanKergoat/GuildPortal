from django import forms

__author__ = 'Alexandre Cloquet'
from .models import Enrollement


class EnrollementForm(forms.ModelForm):
    # characters_choice = forms.CharField(widget=forms.Select())
    class Meta:
        model = Enrollement
        exclude = ()