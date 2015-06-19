from django.contrib.auth.models import User
from django.db import models
from Portal.models import CharacterAttribute, Game, Comment
from django.utils.translation import ugettext as _

# Create your models here.

class OpennedEnrollmentManager(models.Manager):

    def get_queryset(self):
        enrollments = []
        for enrollment in EnrollmentSettings.objects.filter(open=True):
            if enrollment.reach_limit() == False:
                enrollments.append(enrollment)
        return enrollments

class EnrollmentSettings(models.Model):
    '''
        Admin Side enrollment configuration. Allow admin user to define what kind of character they are looking for.
        An object of this class represent a specific kind of character.
        E.g : If you want a Heal on World Of Warcraft and a Tank on World Of Warcraft as well, you need to have instance
        object of this class to match the requirement
    '''
    roles = models.ManyToManyField(CharacterAttribute)
    game_choice = models.ForeignKey(Game)
    open = models.BooleanField(_('Open Enrollment'), default=False)
    limit = models.SmallIntegerField(_('Limit'))
    # Images should be 992*250px
    background_image = models.ImageField(_('Background image'), upload_to='enrollment/background/', blank=True)
    thumbnail = models.ImageField(_('Thumbnail image'), upload_to='enrollment/thumbnail/', blank=True)
    objects = models.Manager()
    openned_enrollement = OpennedEnrollmentManager()

    def __str__(self):
        return u'%s, ' % [" ".join((i.attribute_name.field_value, i.attribute_value.field_value, i.for_game.name)) for i in self.roles.all()]

    def reach_limit(self):
        return False

    class Meta:
        app_label = "PortalEnrollment"
        verbose_name = _('Enrollment settings')
        verbose_name_plural = _('Enrollments settings')

import datetime
class Enrollement(models.Model):
    '''
        Define an enrollment application by a user
        Each object of this class represent an application
    '''
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
    enrollement_date = models.DateField(default=datetime.date.today)
    open = models.BooleanField(_('Open'), default=True)

    class Meta:
        app_label = "PortalEnrollment"
        verbose_name = _('Enrollment')
        verbose_name_plural = _('Enrollments')
        #ordering = ["-enrollment_date"]

    def get_vote_up(self):
        return len(self.enrollmentvote_set.filter(vote=True))


    def get_vote_down(self):
        return len(self.enrollmentvote_set.filter(vote=False))


class EnrollmentVote(models.Model):
    user = models.ForeignKey(User)
    enrollment = models.ForeignKey(Enrollement)
    vote = models.BooleanField(_('Vote'), default=False)
    # 0 refus, 1 accept


class CommentEnrollment(Comment):
    enrollment = models.ForeignKey(Enrollement)