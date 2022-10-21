from django.contrib import admin
from . import models


# Register your models here.

class SongInline(admin.StackedInline):
    model = models.Song
    extra = 0
    min_num = 1


@admin.register(models.Album)
class AlbumAdmin(admin.ModelAdmin):
    inlines = [SongInline]
    list_display = ['artist', 'name', 'created', 'release_datetime',
                    'cost', 'is_approved']
    readonly_fields = ['created']


@admin.register(models.Song)
class SongAdmin(admin.ModelAdmin):
    list_display = ['album', 'name', 'image', 'image_thumbnail', 'audio']
