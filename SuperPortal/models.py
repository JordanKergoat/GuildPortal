from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import ugettext as _

from usersettings.models import UserSettings

class GuildSettings(UserSettings):
    guild_name = models.CharField(_('Guild name'), max_length=120)
    guild_motto = models.CharField(_('Guild motto'), max_length=256)
    guild_chief = models.ForeignKey(User)

    class Meta:
        verbose_name = _('Guild Settings')
        verbose_name_plural = _('Guild Settings')
