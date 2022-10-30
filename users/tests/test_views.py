from rest_framework import status
import pytest
from model_bakery import baker
from users.models import User


@pytest.mark.django_db
class TestRetrieveUser:
    def test_if_user_is_anonymous_return_401(self, auth_client):
        user = baker.make(User)
        response = auth_client.get(f'/users/{user.id}/')
        assert response.status_code == status.HTTP_401_UNAUTHORIZED
