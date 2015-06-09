__author__ = 'Alexandre Cloquet'

from Portal.models import Portal
from SuperPortal.models import GuildSettings

def menu(request):
    return {
        'list_portal': Portal.objects.all()
    }


def guild_info(request):
    return {
        'guild': GuildSettings.objects.all().first()
    }