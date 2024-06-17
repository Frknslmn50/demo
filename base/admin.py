from django.contrib import admin

# Register your models here.

from .models import Poem, Theme, Comment

admin.site.register(Poem)
admin.site.register(Theme)
admin.site.register(Comment)
