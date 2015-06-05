__author__ = 'Alexandre Cloquet'


from django.utils.translation import ugettext as _

from django.db import models


class Portal(models.Model):
    name = models.CharField(_("Portal name"), max_length=100)
    guild_name = models.CharField(_("Portal guild name"), max_length=100, help_text="Can be blank. If blank, we will take guild name from SuperPortal")
    image = models.ImageField(_('Image'), upload_to='/portal/logo/')


