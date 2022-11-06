from random import randint
from .models import Album, Song
from artists.models import Artist
from rest_framework import serializers
from artists.serializers import ArtistSerializer


class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = ['id', 'artist', 'name', 'release_datetime', 'cost']
        artist = ArtistSerializer(read_only=True)

        def create(self, validated_data):
            validated_data['artist'] = Artist.objects.get(
                user=self.context['request'].user)
            return super(AlbumSerializer, self).create(validated_data)


class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ['id', 'album', 'name',  'image', 'audio']
    album = AlbumSerializer()
