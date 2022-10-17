from django.contrib import admin
from . import models


# Register your models here.

class AlbumInline(admin.TabularInline):
    model = models.Album
    extra = 1


@admin.register(models.Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display = ['artist', 'name', 'created', 'release_datetime',
                    'cost', 'is_approved']
    readonly_fields = ['created']
