from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import ugettext as _

# Create your models here.

class CharacterModel(models.Model):
    user = models.ForeignKey(User)
    name = models.CharField(_('Name'), max_length=50)
    iLvl = models.IntegerField(_('iLvl'), default=0)