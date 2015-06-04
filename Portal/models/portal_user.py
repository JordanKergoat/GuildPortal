__author__ = 'Alexandre Cloquet'

from django.utils.translation import ugettext as _
from django.contrib.auth.models import User
from django.db import models
from .enrollment import CharacterAttribute

class Character(models.Model):
    user = models.ForeignKey(User)
    roles = models.ManyToManyField(CharacterAttribute)


class Absence(models.Model):
    user = models.ForeignKey(User)
    status = models.BooleanField(_('On holiday'), default=False)
    from_date = models.DateField()
    to_date = models.DateField()
    reason = models.TextField(_('Reason'))


STATUS_USER = (
    (_("Active"), _("Active")),
    (_("Inactive"), _("Inactive")),
    (_("Absent"), _("Absent")),
)

class Userprofile(models.Model):
    user = models.OneToOneField(User)
    birthday_date = models.DateField(_('Birthday date'))
    job_study = models.TextField(_("Job/Study"))
    status = models.CharField(_('Member status'), choices=STATUS_USER, max_length=64)
    country = models.CharField(_('Country'), max_length=50)
    town = models.CharField(_('Town'), max_length=256)
    teamspeak_nickname = models.CharField(_("TeamSpeak Nickname"), max_length=64, blank=True)
    mumble_nickname = models.CharField(_("Mumble Nickname"), max_length=64, blank=True)
    skype_nickname = models.CharField(_("Skype Nickname"), max_length=64, blank=True)