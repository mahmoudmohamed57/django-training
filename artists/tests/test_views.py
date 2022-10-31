from rest_framework import status
import pytest
from model_bakery import baker
from artists.models import Artist


@pytest.mark.django_db
class TestCreateArtist:
    def test_if_artists_are_found_return_200(self, auth_client):
        response = auth_client.get('/artists/')
        assert response.status_code == status.HTTP_200_OK

    def test_if_artist_is_found_return_200(self, auth_client):
        artist = baker.make(Artist)
        response = auth_client.get(f'/artists/{artist.id}/')
        assert response.status_code == status.HTTP_200_OK
