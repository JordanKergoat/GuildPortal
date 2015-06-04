from django.contrib.auth.models import User
from django.db import models
from Portal.models import CharacterAttribute, Game
from django.utils.translation import ugettext as _

# Create your models here.

class EnrollmentSettings(models.Model):
    roles = models.ManyToManyField(CharacterAttribute)
    open = models.BooleanField(_('Open Enrollment'), default=False)
    limit = models.SmallIntegerField(_('Limit'))
    background_image = models.ImageField(_('Background image'), upload_to='/enrollment/background/', blank=True)
    thumbnail = models.ImageField(_('Thumbnail image'), upload_to='/enrollment/thumbnail/', blank=True)

    def __unicode__(self):
        return u'%s, ' % [" ".join((i.attribute_name, i.attribute_value.field_value, i.for_game.name)) for i in self.roles.all()]

    def reach_limit(self):
        pass

    class Meta:
        app_label = "PortalEnrollment"
        verbose_name = _('Enrollment settings')
        verbose_name_plural = _('Enrollments settings')


class Enrollement(models.Model):
    user = models.ForeignKey(User)
    introduction = models.TextField()
    game_choice = models.ForeignKey(Game)
    roles = models.ManyToManyField(CharacterAttribute)
    age = models.SmallIntegerField(_('Your age'))
    character_name = models.CharField(max_length=50)
    another_characters = models.BooleanField(_('Another characters'), default=False)
    availability = models.TextField(_('Availabilities'))
    motivations = models.TextField(_('Motivations'))
    experience_PVE = models.TextField(_('Experiences PVE'))
    experience_PVP = models.TextField(_('Experiences PVP'))
    old_guild = models.TextField(_('Old Guilds'))

    class Meta:
        app_label = "PortalEnrollment"
        verbose_name = _('Enrollment')
        verbose_name_plural = _('Enrollments')