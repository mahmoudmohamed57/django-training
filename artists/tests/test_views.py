import pytest
from rest_framework import status


@pytest.mark.django_db
class TestCreateArtist:
    def test_if_artists_are_found_return_200(self, auth_client, artist):
        response = auth_client.get('/artists/')
        assert response.status_code == status.HTTP_200_OK
        assert response.data == [
            {'id': artist.id, 'stage_name': artist.stage_name,
                'social_link_field': artist.social_link_field}]

    def test_if_artist_is_found_return_200(self, auth_client, artist):
        response = auth_client.get(f'/artists/{artist.id}/')
        assert response.status_code == status.HTTP_200_OK
        assert response.data == {'id': artist.id, 'stage_name': artist.stage_name,
                                 'social_link_field': artist.social_link_field}
