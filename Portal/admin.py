from django.contrib import admin

# Register your models here.

from .models.enrollment import *
from .models.portal_guild import *
from .models.news import *

admin.site.register(FieldValue)
admin.site.register(CharacterAttribute)
admin.site.register(Game)
admin.site.register(Portal)
admin.site.register(News)
admin.site.register(Category)
admin.site.register(Tag)
