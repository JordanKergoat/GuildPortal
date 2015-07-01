from django.contrib import admin

# Register your models here.
from Forum.models import Forum, Category, Thread, Post

admin.site.register(Forum)
admin.site.register(Category)
admin.site.register(Thread)
admin.site.register(Post)