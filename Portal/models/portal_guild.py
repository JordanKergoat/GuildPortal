__author__ = 'Alexandre Cloquet'


from django.utils.translation import ugettext as _


from django.contrib.auth.models import User
from django.db import models



class Guild(models.Model):
    guild_name = models.CharField(_('Guild name'), max_length=120)
    guild_motto = models.CharField(_('Guild motto'), max_length=256)
    guild_chief = models.ForeignKey(User)