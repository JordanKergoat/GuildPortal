from django.contrib import admin
from django.http import HttpResponseRedirect

from .models import GuildSettings
from usersettings.admin import SettingsAdmin
from django.utils.translation import ugettext_lazy as _


class GuildSettingsAdmin(admin.ModelAdmin):
    def add_view(self, request, form_url='', extra_context=None):
        if request.method == "POST":
            # Assuming you want a single, global HomePage object
            if GuildSettings.objects.count() >= 1:
                # redirect to a page saying
                # you can't create more than one
                return HttpResponseRedirect("foo")
        return super(GuildSettingsAdmin, self).add_view(request, form_url, extra_context)

    def has_add_permission(self, request):
        if GuildSettings.objects.count() >= 1:
            return False
        return True

admin.site.register(GuildSettings, GuildSettingsAdmin)