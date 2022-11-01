import pytest
from rest_framework.test import APIClient
from model_bakery import baker
from knox.models import AuthToken
from artists.models import Artist
from users.models import User


@pytest.fixture
def artist():
    return baker.make(Artist)


@pytest.fixture
def user():
    return baker.make(User)


@pytest.fixture
def auth_client(user):
    client = APIClient()
    token = AuthToken.objects.create(user=user)[1]
    client.credentials(HTTP_AUTHORIZATION='Token ' + token)
    return client
