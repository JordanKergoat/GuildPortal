__author__ = 'Alexandre Cloquet'


from django.utils.translation import ugettext as _

from django.db import models
from SuperPortal.models import SuperPortal


class Portal(models.Model):
    portal = models.ForeignKey(SuperPortal, blank=True, null=True)
    active = models.BooleanField(_('Active ?'), default=True)
    name = models.CharField(_("Portal name"), max_length=100)
    guild_name = models.CharField(_("Portal guild name"), max_length=100, help_text="Can be blank. If blank, we will take guild name from SuperPortal")
    image = models.ImageField(_('Image'), upload_to='portal/logo/')

    def get_absolute_url(self):
        from django.core.urlresolvers import reverse
        return reverse('Portal.views.index', args=[str(self.name)])

    def __str__(self):
        return u"%s - %s" % (self.guild_name, self.name)