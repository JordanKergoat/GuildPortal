from PortalMessaging.models import Message

__author__ = 'Alexandre Cloquet'

from Portal.models import Portal
from SuperPortal.models import GuildSettings, SuperPortal
from PortalEnrollment.models import Enrollement

def menu(request):
    return {
        'list_portal': Portal.objects.all(),
        'messages_number': Message.objects.filter(receiver=request.user,
                                                  time_read=None).count()
    }


def guild_info(request):
    if request.user.is_authenticated():
        if GuildSettings.objects.all().first():
            for group in GuildSettings.objects.all().first().group_can_vote.all():
                if group in request.user.groups.all():
                    return {
                        'guild': GuildSettings.objects.all().first(),
                        'super_portal': SuperPortal.objects.all().first(),
                        'number_enrollment': len(Enrollement.objects.filter(open=True)),

                    }
    return {
        'guild': GuildSettings.objects.all().first(),
        'super_portal': SuperPortal.objects.all().first()
    }