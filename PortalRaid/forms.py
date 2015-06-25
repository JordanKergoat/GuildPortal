from Portal.models import CharacterAttribute, TypeValue
from PortalRaid.models import CharacterModel, CharacterForOutRaid

__author__ = 'Alexandre Cloquet'

from django import forms

class CharacterForm(forms.ModelForm):
    class Meta:
        model = CharacterModel
        exclude = ('user', 'iLvl', 'url')
        widgets = {
            'game': forms.Select(attrs={
                'onchange': "serverAPI(this.value, this.id)"
            })
        }

class CharactersRaidForm(forms.ModelForm):
    class Meta:
        model = CharacterForOutRaid
        exclude = ()
        widgets = {
            'character': forms.Select(attrs={
                'onchange': "classforCharacterAPI(this.value, this.id)"
            })
        }