import pytest
from rest_framework import status


@pytest.mark.django_db
class TestCreateRegister:
    def test_if_data_is_valid_return_201(self, auth_client):
        user_data = {"username": "Mahmoud", "email": "mahmoud@domain.com",
                     "password1": "Mahmoudali", "password2": "Mahmoudali"}
        response = auth_client.post('/authentication/register/', user_data)
        assert response.status_code == status.HTTP_201_CREATED
        assert response.data == {
            "username": "Mahmoud", "email": "mahmoud@domain.com"}

    def test_if_data_is_invalid_return_400(self, auth_client):
        user_data = {"username": "Mahmoud", "email": "mahmoud@domain.com",
                     "password1": "Mahmoudali"}
        response = auth_client.post('/authentication/register/', user_data)
        assert response.status_code == status.HTTP_400_BAD_REQUEST


@pytest.mark.django_db
class TestCreateLogin:
    def test_if_data_is_ok_return_200(self, auth_client):
        user_data = {"username": "Mahmoud", "email": "mahmoud@domain.com",
                     "password1": "Mahmoudali", "password2": "Mahmoudali"}
        auth_client.post(
            '/authentication/register/', user_data)
        response = auth_client.post(
            '/authentication/login/', {"username": "Mahmoud", "password": "Mahmoudali"})
        assert response.status_code == status.HTTP_200_OK

    def test_if_data_is_invalid_return_400(self, auth_client):
        user_data = {"username": "Mahmoud", "email": "mahmoud@domain.com",
                     "password1": "Mahmoudali", "password2": "Mahmoudali"}
        auth_client.post(
            '/authentication/register/', user_data)
        response = auth_client.post('/authentication/login/',
                                    {"username": "Mahmoud"})
        assert response.status_code == status.HTTP_400_BAD_REQUEST


@pytest.mark.django_db
class TestCreateLogout:
    def test_if_no_content_return_204(self, auth_client):
        response = auth_client.post('/authentication/logout/')
        assert response.status_code == status.HTTP_204_NO_CONTENT
