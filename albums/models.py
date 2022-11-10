from django.db import models
from django.core.validators import FileExtensionValidator
from django import forms
from artists.models import Artist
from model_utils.models import TimeStampedModel
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
from .tasks import send_artist_a_congratulation_email


# Create your models here.

class ApprovedAlbumManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_approved=True)


class Album(TimeStampedModel):
    artist = models.ForeignKey(Artist, null=False, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, default="New Album")
    release_datetime = models.DateTimeField(blank=False)
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    is_approved = models.BooleanField(
        default=True, help_text='Approve the album if its name is not explicit')
    objects = models.Manager()
    approved_album = ApprovedAlbumManager()

    def save(self, *args, **kwargs):
        send_artist_a_congratulation_email.delay(self.artist.user.id, self.name, self.release_datetime, self.cost)
        super(Album, self).save(*args, **kwargs)

    def __str__(self):
        return (f"name = {self.name} || creation_datetime = {self.created} || release_datetime = {self.release_datetime} || cost = {self.cost}")


class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, blank=True)
    image = models.ImageField(blank=False, upload_to="images/")
    image_thumbnail = ImageSpecField(
        source='image', format="JPEG", processors=[ResizeToFill(100, 50)])
    # Do you think this field is useful?
    # I think this field is useful because If someone has a lot of images to look through, thumbnails can help them find an image they want faster since they don't have to open each file individually.
    audio = models.FileField(blank=False, upload_to="audio/", validators=[
                             FileExtensionValidator(allowed_extensions=['mp3', 'wav'])])

    def __str__(self):
        return (f"name = {self.name} || image = {self.image} || image_thumbnail = {self.image_thumbnail} || audio = {self.audio}")

    def save(self):
        if self.name == "":
            self.name = self.album.name
        return super().save()

    def delete(self, *args, **kwargs):
        if (self.album.song_set.all().count() > 1):
            super(Song, self).delete(*args, **kwargs)
        else:
            raise forms.ValidationError(
                "You can't delete all songs from an album, There must be one song at least.")
