from django.contrib import admin
from . import models


# Register your models here.


@admin.register(models.Artist)
class ArtistAdmin(admin.ModelAdmin):
    list_display = ['stage_name', 'social_link_field', 'approved_albums']
