__author__ = 'Alexandre Cloquet'

from django.utils.translation import ugettext as _


from django.contrib.auth.models import User
from django.db import models

class Game(models.Model):
    name = models.CharField(max_length=128)
    image = models.ImageField(upload_to='game/', blank=True)
    image_thumbnail = models.ImageField(upload_to='game/thumbnail/', blank=True)

    class Meta:
        verbose_name = _('Game')
        verbose_name_plural = _('Games')

    def __str__(self):
        return self.name

class Class(models.Model):
    name = models.CharField(max_length=64)
    game = models.ForeignKey(Game)

    class Meta:
        verbose_name = _('Class')
        verbose_name_plural = _('Class')

    def __str__(self):
        return self.name


class FieldValue(models.Model):

    field_value = models.CharField(max_length=64)

    def __str__(self):
        return self.field_value

class CharacterAttribute(models.Model):

    attribute_name = models.CharField(max_length=64)
    attribute_value = models.ForeignKey(FieldValue)
    for_game = models.ForeignKey(Game)

    def __str__(self):
        return '[' + self.for_game.name + '] ' + self.attribute_name + ' - ' +  self.attribute_value.field_value