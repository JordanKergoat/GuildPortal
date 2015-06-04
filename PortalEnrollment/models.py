from django.db import models
from Portal.models import CharacterAttribute
from django.utils.translation import ugettext as _

# Create your models here.

class Enrollment(models.Model):
    roles = models.ManyToManyField(_('Role'), CharacterAttribute)
    open = models.BooleanField(_('Open Enrollment'), default=False)
    limit = models.SmallIntegerField(_('Limit'))
    background_image = models.ImageField(_('Background image'), upload_to='/enrollment/background/', blank=True)
    thumbnail = models.ImageField(_('Thumbnail image'), upload_to='/enrollment/thumbnail/', blank=True)

    def reach_limit(self):
        pass

    class Meta:
        verbose_name = _('Enrollment')
        verbose_name_plural = _('Enrollments')