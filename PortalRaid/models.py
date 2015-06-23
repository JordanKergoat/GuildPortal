from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import ugettext as _

# Create your models here.
from Portal.models import Game


class CharacterModel(models.Model):
    user = models.ForeignKey(User)
    game = models.ForeignKey(Game, blank=True, null=True)
    name = models.CharField(_('Name'), max_length=50)
    server = models.ForeignKey('Realm')
    iLvl = models.IntegerField(_('iLvl'), default=0, null=True)
    url = models.URLField(null=True, blank=True)

    def __str__(self):
        return "%s: %s - %s : %s" % (self.user.username, self.name, self.game.name, self.server.name)

    class Meta:
        ordering = ('user',)
        verbose_name = _('Character')
        verbose_name_plural = _('Characters')


class Realm(models.Model):
    #TODO Faire une update admin pour remplir automatiquement
    game = models.ForeignKey(Game, blank=True, null=True)
    name = models.CharField(_('Realm name'), max_length=50)

    def __str__(self):
        return "%s - %s" %(self.game, self.name)

    class Meta:
        ordering = ('game',)
        verbose_name = _('Realm')
        verbose_name_plural = _('Realms')