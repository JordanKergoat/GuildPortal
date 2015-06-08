from django.contrib.auth.models import User, Group
from django.db import models
from django.utils.translation import ugettext as _
from uuid import uuid4

class GuildSettings(models.Model):
    guild_name = models.CharField(_('Guild name'), max_length=120)
    guild_motto = models.CharField(_('Guild motto'), max_length=256)
    guild_chief = models.ForeignKey(User)
    short_guild_description = models.CharField(_("Short description about your guild"), max_length=120, default="")
    guild_description = models.TextField(_("Description about your guild"), default="")
    tag = models.CharField(_('Tag'), max_length=10, default="")
    group_can_vote = models.ManyToManyField(Group, blank=True, related_name='group_can_vote')
    group_can_write_news = models.ManyToManyField(Group, blank=True, related_name='group_can_write_news')
    group_can_write_wiki = models.ManyToManyField(Group, blank=True, related_name='group_can_write_wiki')

    class Meta:
        verbose_name = _('Guild Settings')
        verbose_name_plural = _('Guild Settings')

    def __str__(self):
        return u"[%s][%s] %s - %s" % (self.tag, self.guild_name, self.guild_motto, self.guild_chief.username)



class SuperPortal(models.Model):
    id_uuid = models.CharField(max_length=36, primary_key=True,
                          default=str(uuid4()), editable=False)
