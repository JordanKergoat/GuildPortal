__author__ = 'Alexandre Cloquet'

from django.utils.translation import ugettext as _


from django.contrib.auth.models import User
from django.db import models

class Game(models.Model):
    name = models.CharField(max_length=128)
    image = models.ImageField(upload_to='game/', blank=True)
    url_api = models.URLField(blank=True, null=True)
    image_thumbnail = models.ImageField(upload_to='game/thumbnail/', blank=True)

    class Meta:
        verbose_name = _('Game')
        verbose_name_plural = _('Games')

    def __str__(self):
        return self.name

    def get_out_raid(self):
        list_out_raid = []
        for raid in self.raid_set.all():
            for out_raid in raid.get_out_raid():
                list_out_raid.append(out_raid)
        return list_out_raid


    def percent_of_player(self):
        all_user_for_game = len(self.userprofile_set.all())
        all_user = len(User.objects.all()) - 1
        return float((all_user_for_game * 100) / all_user)

class Class(models.Model):
    name = models.CharField(max_length=64)
    game = models.ForeignKey(Game)

    class Meta:
        verbose_name = _('Class')
        verbose_name_plural = _('Class')

    def __str__(self):
        return self.name


class FieldValue(models.Model):

    field_value = models.CharField(_('value'), max_length=64)

    def __str__(self):
        return self.field_value

    class Meta:
        verbose_name = _('Table entry')
        verbose_name_plural = _('Tables entries')

class TypeValue(models.Model):
    field_value = models.CharField(_('value'), max_length=64)
    game = models.ForeignKey(Game, null=True)

    def __str__(self):
        return self.field_value

    class Meta:
        verbose_name = _('Table name')
        verbose_name_plural = _('Tables names')

class CharacterAttribute(models.Model):

    attribute_name = models.ForeignKey(TypeValue)
    attribute_value = models.ForeignKey(FieldValue)
    for_game = models.ForeignKey(Game, null=True)

    def __str__(self):
        return '[' + self.for_game.name + '] ' + self.attribute_name.field_value + ' - ' +  self.attribute_value.field_value

    class Meta:
        verbose_name = _('Table relation')
        verbose_name_plural = _('Tables relations')