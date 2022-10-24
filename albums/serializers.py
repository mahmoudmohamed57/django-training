from .models import Album, Song
from rest_framework import serializers


class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = ['id', 'name',  'created',
                  'release_datetime', 'cost', 'is_approved']


class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ['id', 'name',  'image', 'audio']

    def create(self, validated_data):
        album_id = self.context('album_id')
        return Song.objects.create(album_id=album_id, **validated_data)
