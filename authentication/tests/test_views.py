from rest_framework import status
import pytest


@pytest.mark.django_db
class TestCreateRegister:
    def test_if_data_is_valid_return_201(self, auth_client):
        response = auth_client.post(
            '/authentication/register/', {"username": "Mahmoud", "email": "mahmoud@domain.com",
                                          "password1": "Mahmoudali", "password2": "Mahmoudali"})
        assert response.status_code == status.HTTP_201_CREATED

    def test_if_data_is_invalid_return_400(self, auth_client):
        response = auth_client.post(
            '/authentication/register/', {"username": "Mahmoud", "email": "mahmoud@domain.com",
                                          "password1": "Mahmoudali"})
        assert response.status_code == status.HTTP_400_BAD_REQUEST


@pytest.mark.django_db
class TestCreateLogin:
    def test_if_data_is_ok_return_200(self, auth_client):
        auth_client.post(
            '/authentication/register/', {"username": "Mahmoud", "email": "mahmoud@domain.com",
                                          "password1": "Mahmoudali", "password2": "Mahmoudali"})
        response = auth_client.post(
            '/authentication/login/', {"username": "Mahmoud", "password": "Mahmoudali"})
        assert response.status_code == status.HTTP_200_OK

    def test_if_data_is_invalid_return_400(self, auth_client):
        auth_client.post(
            '/authentication/register/', {"username": "Mahmoud", "email": "mahmoud@domain.com",
                                          "password1": "Mahmoudali", "password2": "Mahmoudali"})
        response = auth_client.post('/authentication/login/',
                                    {"username": "Mahmoud"})
        assert response.status_code == status.HTTP_400_BAD_REQUEST


@pytest.mark.django_db
class TestCreateLogout:
    def test_if_no_content_return_204(self, auth_client):
        auth_client.post(
            '/authentication/register/', {"username": "Mahmoud", "email": "mahmoud@domain.com",
                                          "password1": "Mahmoudali", "password2": "Mahmoudali"})
        data = auth_client.post(
            '/authentication/login/', {"username": "Mahmoud", "password": "Mahmoudali"})
        auth_client.credentials(
            HTTP_AUTHORIZATION='TOKEN ' + data.data["token"])
        response = auth_client.post('/authentication/logout/')
        assert response.status_code == status.HTTP_204_NO_CONTENT

    def test_if_user_is_anonymous_return_401(self, auth_client):
        response = auth_client.post('/authentication/logout/')
        assert response.status_code == status.HTTP_401_UNAUTHORIZED
