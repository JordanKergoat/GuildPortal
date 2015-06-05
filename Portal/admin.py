from django.contrib import admin

# Register your models here.

from .models.enrollment import *
from .models.portal_guild import *

admin.site.register(FieldValue)
admin.site.register(CharacterAttribute)
admin.site.register(Game)
