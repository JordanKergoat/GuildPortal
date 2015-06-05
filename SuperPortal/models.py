from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import ugettext as _

class GuildSettings(models.Model):
    guild_name = models.CharField(_('Guild name'), max_length=120)
    guild_motto = models.CharField(_('Guild motto'), max_length=256)
    guild_chief = models.ForeignKey(User)
    short_guild_description = models.CharField(_("Short description about your guild"), max_length=120, default="")
    guild_description = models.TextField(_("Description about your guild"), default="")

    class Meta:
        verbose_name = _('Guild Settings')
        verbose_name_plural = _('Guild Settings')

    def __unicode__(self):
        return u"[%s] %s - %s" % (self.guild_name, self.guild_motto, self.guild_chief.username)
