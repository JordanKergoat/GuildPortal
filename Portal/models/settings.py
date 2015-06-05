__author__ = 'Alexandre Cloquet'

from django.db import models
from django.utils.translation import ugettext_lazy as _

from usersettings.models import UserSettings

class SiteSettings(UserSettings):
    site_title = models.CharField(_('Site Title'), max_length=100)
    tag_line = models.CharField(_('Tag Line'), max_length=150, blank=True)
    site_description = models.TextField(_('Site Description'), blank=True)

    class Meta:
        verbose_name = 'Site Settings'
        verbose_name_plural = 'Site Settings'