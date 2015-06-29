from Portal.models import CommentNews

__author__ = 'Alexandre Cloquet'


from django import forms
from .models import Enrollement, EnrollmentSettings, CommentEnrollment

class OpenEnrollementForm(forms.ModelForm):
    class Meta:
        model = Enrollement
        exclude = ('user', 'roles', 'enrollement_date')
        widgets = {
            'game_choice': forms.Select(attrs={
                'onchange' : "charactersAPI(this.value, this.id)"
            })
        }


class EnrollementForm(forms.ModelForm):
    class Meta:
        model = Enrollement
        exclude = ('user', 'game_choice', 'enrollement_date', 'roles')


class CommentEnrollmentForm(forms.ModelForm):
    class Meta:
        model = CommentEnrollment
        exclude = ('user', 'enrollment', 'response')


class CommentNewsForm(forms.ModelForm):
    class Meta:
        model = CommentNews
        exclude = ('user', 'news', 'response')