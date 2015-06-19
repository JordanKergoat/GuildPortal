__author__ = 'Alexandre Cloquet'

from django.contrib.auth.models import User, Group
from django.db import models
from django.utils.translation import ugettext as _
from uuid import uuid4


from Portal.models import Category


class GuildSettings(models.Model):
    '''
    Handle all settings about guild and SuperPortal
    '''
    guild_name = models.CharField(_('Guild name'), max_length=120)
    guild_motto = models.CharField(_('Guild motto'), max_length=256)
    guild_chief = models.ForeignKey(User)
    short_guild_description = models.CharField(_("Short description about your guild"), max_length=120, default="")
    guild_description = models.TextField(_("Description about your guild"), default="")
    tag = models.CharField(_('Tag'), max_length=10, default="")
    forum_active = models.BooleanField(_('Forum active'), default=True)
    slider_active = models.BooleanField(_('Slider active'), default=False)
    youtube_channel = models.URLField(_('Youtube channel'), default="", blank=True, null=True)
    twitch_channel = models.CharField(_('Twitch channel'), default="", blank=True, null=True, max_length=50)
    facebook_page = models.URLField(_('Facebook Page'), default="", blank=True, null=True)
    twitter_page = models.URLField(_('Twitter page'), default="", blank=True, null=True)
    category_slider = models.ForeignKey(Category, blank=True, null=True)
    group_can_vote = models.ManyToManyField(Group, blank=True, related_name='group_can_vote')
    group_can_write_news = models.ManyToManyField(Group, blank=True, related_name='group_can_write_news')
    group_can_write_wiki = models.ManyToManyField(Group, blank=True, related_name='group_can_write_wiki')
    icon_guild = models.ImageField(upload_to='superportal/setting', blank=True, null=True)

    class Meta:
        verbose_name = _('Guild Settings')
        verbose_name_plural = _('Guild Settings')

    def __str__(self):
        return u"[%s][%s] %s - %s" % (self.tag, self.guild_name, self.guild_motto, self.guild_chief.username)