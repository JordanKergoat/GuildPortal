__author__ = 'Alexandre Cloquet'


from django import forms
from .models import Enrollement, EnrollmentSettings

class OpenEnrollementForm(forms.ModelForm):
    class Meta:
        model = Enrollement
        exclude = ('user', 'roles')
        widgets = {
            'game_choice': forms.Select(attrs={
                'onchange' : "charactersAPI(this.value, this.id)"
            })
        }


class EnrollementForm(forms.ModelForm):
    class Meta:
        model = Enrollement
        exclude = ('user', 'game_choice')