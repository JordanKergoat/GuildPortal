from django.contrib import admin

from .models import GuildSettings
from usersettings.admin import SettingsAdmin
from django.utils.translation import ugettext_lazy as _


class GuildSettingsAdmin(SettingsAdmin):

    fieldsets = (
        (_('Site Title / Tag Line'), {
            'description': '...',
            'fields': ('guild_name', 'guild_motto', 'guild_chief',)
        }),
    )

admin.site.register(GuildSettings, GuildSettingsAdmin)