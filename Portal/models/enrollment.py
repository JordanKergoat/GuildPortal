__author__ = 'Alexandre Cloquet'

from django.utils.translation import ugettext as _


from django.contrib.auth.models import User
from django.db import models

class Game(models.Model):
    name = models.CharField(max_length=128)

    class Meta:
        verbose_name = _('Game')
        verbose_name_plural = _('Games')

    def __unicode__(self):
        return self.name

class Class(models.Model):
    name = models.CharField(max_length=64)
    game = models.ForeignKey(Game)

    class Meta:
        verbose_name = _('Class')
        verbose_name_plural = _('Class')

    def __unicode__(self):
        return self.name


class FieldValue(models.Model):

    field_value = models.CharField(max_length=64)

    def __unicode__(self):
        return self.field_value

class FieldName(models.Model):

    field_name = models.CharField(max_length=64)
    field_value = models.ForeignKey(FieldValue)
    related_to = models.ForeignKey(Game)

    def __unicode__(self):
        return '[' + self.related_to.name + '] ' + self.field_name + ' - ' +  self.field_value.field_value

class Enrollement(models.Model):
    user = models.ForeignKey(User)
    introduction = models.TextField()
    game_choice = models.ForeignKey(Game)
    character_name = models.CharField(max_length=50)
