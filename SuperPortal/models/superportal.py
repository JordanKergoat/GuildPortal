from uuid import uuid4

__author__ = 'Alexandre Cloquet'

from django.db import models
from django.utils.translation import ugettext as _


class SuperPortal(models.Model):
    id_uuid = models.CharField(max_length=36, primary_key=True,
                          default=str(uuid4()), editable=False)
    banner = models.ImageField(_('Banner'), upload_to='superportal/banner', blank=True, null=True)