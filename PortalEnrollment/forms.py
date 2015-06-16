__author__ = 'Alexandre Cloquet'


from django import forms
from .models import Enrollement, EnrollmentSettings

class EnrollementForm(forms.ModelForm):
    class Meta:
        model = Enrollement
        exclude = ('user',)