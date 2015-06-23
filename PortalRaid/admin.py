from django.contrib import admin

# Register your models here.
from PortalRaid.models import Realm, CharacterModel

admin.site.register(Realm)
admin.site.register(CharacterModel)