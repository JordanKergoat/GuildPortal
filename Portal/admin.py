from django.contrib import admin

# Register your models here.

from .models.enrollment import *
from .models.portal_guild import *
from django.utils.translation import ugettext_lazy as _


from usersettings.admin import SettingsAdmin

from .models import SiteSettings


class SiteSettingsAdmin(SettingsAdmin):

    fieldsets = (
        (_('Site Title / Tag Line'), {
            'description': '...',
            'fields': ('site_title', 'tag_line',)
        }),
    )

admin.site.register(SiteSettings, SiteSettingsAdmin)
admin.site.register(FieldValue)
admin.site.register(CharacterAttribute)
admin.site.register(Game)
admin.site.register(Guild)