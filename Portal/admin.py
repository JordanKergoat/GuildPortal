from django.contrib import admin

# Register your models here.

from .models.enrollment import *

admin.site.register(FieldValue)
admin.site.register(FieldName)
admin.site.register(Game)