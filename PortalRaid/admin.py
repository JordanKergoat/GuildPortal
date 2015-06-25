from django.contrib import admin

# Register your models here.
from PortalRaid.models import Realm, CharacterModel, GroupForRaid, OutRaid, RaidLvl, Boss, Raid, ClassForOutRaid, \
    CharacterForOutRaid

admin.site.register(Realm)
admin.site.register(Raid)
admin.site.register(CharacterModel)
admin.site.register(Boss)
admin.site.register(RaidLvl)
admin.site.register(GroupForRaid)
admin.site.register(OutRaid)
admin.site.register(ClassForOutRaid)
admin.site.register(CharacterForOutRaid)