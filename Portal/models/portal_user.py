from PortalRaid.models import OutRaid

__author__ = 'Alexandre Cloquet'

from django.utils.translation import ugettext as _
from django.contrib.auth.models import User
from django.db import models
from .enrollment import CharacterAttribute, Game


class Character(models.Model):
    '''
        Keep all characters from user for each game in database
    '''
    user = models.ForeignKey(User)
    game = models.ForeignKey(Game, default="")
    main_character = models.BooleanField(_("Main character"), default=False, help_text="You can specify if this character is your main")
    level = models.SmallIntegerField(_('Character level'), blank=True, help_text="Specify your character level", default=0)
    roles = models.ManyToManyField(CharacterAttribute)


class Absence(models.Model):
    '''
        Allows to save user absence in database
    '''
    user = models.ForeignKey(User)
    status = models.BooleanField(_('On holiday'), default=False, help_text="")
    from_date = models.DateField(_('From'), help_text="Please use the following format: DD-MM-YYYY")
    to_date = models.DateField(_('to'), help_text="Please use the following format: DD-MM-YYYY")
    reason = models.TextField(_('Reason'), help_text="You can explain why you are absent")


STATUS_USER = (
    (_("Active"), _("Active")),
    (_("Inactive"), _("Inactive")),
    (_("Absent"), _("Absent")),
)

GENDER_CHOICE = (
    (_('Man'), _('Man')),
    (_('Woman'), _('Woman'))
)


class Userprofile(models.Model):
    user = models.OneToOneField(User)
    birthday_date = models.DateField(_('Birthday date'), blank=True, null=True)
    gender = models.CharField(_('Gender'), choices=GENDER_CHOICE, max_length=50, default=_('Man'))
    job_study = models.TextField(_("Job/Study"))
    status = models.CharField(_('Member status'), choices=STATUS_USER, max_length=64)
    country = models.CharField(_('Country'), max_length=50)
    town = models.CharField(_('Town'), max_length=256)
    teamspeak_nickname = models.CharField(_("TeamSpeak Nickname"), max_length=64, blank=True)
    mumble_nickname = models.CharField(_("Mumble nickname"), max_length=64, blank=True)
    skype_nickname = models.CharField(_("Skype nickname"), max_length=64, blank=True)
    twitch_page = models.CharField(_("Twitch page"), max_length=64, blank=True)
    dailymotion_stream_page = models.CharField(_("Dailymotion stream page"), max_length=64, blank=True)
    games = models.ManyToManyField(Game, verbose_name=_('Games you play ?'))
    about_you = models.TextField(_('About you'), default="")
    image_profile = models.ImageField(_('Image profile'), upload_to='profile/', blank=True, null=True)
    reponse_to_blog = models.IntegerField(default=0, editable=False)
    post_in_forum = models.IntegerField(default=0, editable=False)
    participate_to_raid = models.IntegerField(default=0, editable=False)

    def __str__(self):
        return "%s" % self.user.username

    def get_participation_for_raids(self):
        for raid in OutRaid.objects.all():
            for character in raid.characterforoutraid_set.all():
                if character.character in self.user.charactermodel_set.all():
                    print(character.character, raid.raid.name)


    def age(self):
        import datetime
        return int((datetime.date.today() - self.birthday_date).days / 365.25)

from django.db.models.signals import post_save

def create_profile(sender, **kw):
    user = kw["instance"]
    if kw["created"]:
        up = Userprofile(user=user)
        up.save()

post_save.connect(create_profile, sender=User)