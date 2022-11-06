import pytest
from django.http import HttpRequest
from ..serializers import AlbumSerializer


@pytest.mark.django_db
class TestCreateArtist:
    def test_if_album_is_serializer(self, album):
        serializer = AlbumSerializer(album)
        assert set(serializer.data.keys()) == set(
            ['id', 'artist', 'name', 'release_datetime', 'cost'])
        assert serializer.data['id'] == album.id
        assert serializer.data['artist'] == album.artist.id

    def test_if_album_is_deserializer(self, album):
        request = HttpRequest()
        request.method = 'POST'
        request.user = album.artist.user
        album_data = {
            'artist': album.artist,
            'name': album.name,
            'release_datetime': album.release_datetime,
            'cost': album.cost
        }
        serializer = AlbumSerializer(context={'request': request})
        album_instance = serializer.create(album_data)
        assert album_instance.artist == album.artist
        assert album_instance.name == album.name
        assert album_instance.release_datetime == album.release_datetime
        assert album_instance.cost == album.cost
