from django.contrib import admin
from . import models
from albums.admin import AlbumInline


# Register your models here.


@admin.register(models.Artist)
class ArtistAdmin(admin.ModelAdmin):
    inlines = [AlbumInline]
    list_display = ['stage_name', 'social_link_field', 'approved_albums']
