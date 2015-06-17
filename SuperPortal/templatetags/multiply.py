from django.contrib.auth.models import Group
from SuperPortal.models import GuildSettings
__author__ = 'Jordan'

from django.template import Library

register = Library()


@register.filter
def multiply(a, b):
    return a * b


@register.filter(name='has_group')
def has_group(user, group_name):
    group = Group.objects.get(name=group_name)
    return True if group in user.groups.all() else False


@register.filter(name='can_vote')
def can_vote(user):
    for group in  GuildSettings.objects.all().first().group_can_vote.all():
        if group in user.groups.all():
            return True
    return False