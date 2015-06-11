__author__ = 'Alexandre Cloquet'

from Portal.models import Portal
from SuperPortal.models import GuildSettings, SuperPortal

def menu(request):
    return {
        'list_portal': Portal.objects.all()
    }


def guild_info(request):
    return {
        'guild': GuildSettings.objects.all().first(),
        'super_portal': SuperPortal.objects.all().first()
    }