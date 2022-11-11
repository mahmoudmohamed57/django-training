import pytest
from rest_framework import status
from ..models import Album
from ..serializers import AlbumSerializer


@pytest.mark.django_db
class TestCreateArtist:
    def test_if_view_is_use_expected_serializer(self, auth_client):
        response = auth_client.get('/albums/')
        assert response.data['results'] == AlbumSerializer(
            Album.objects.all(), many=True).data

    def test_if_albums_are_found_return_200(self, auth_client):
        response = auth_client.get('/albums/')
        assert response.status_code == status.HTTP_200_OK

    def test_if_album_are_found_return_200(self, auth_client, album):
        response = auth_client.get(f'/albums/{album.id}/')
        assert response.status_code == status.HTTP_200_OK
