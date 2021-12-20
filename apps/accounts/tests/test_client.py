from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient

from apps.accounts.models.user import User
from apps.accounts.serializers import UserSerializer

BASE_URL = "/api/users/"

REGULARUSER_DATA = {
    "email": "user22@gmail.com",
    "first_name": "First",
    "last_name": "Lasts",
    "password": "superuser",
    "profile": {
        "phone": "671870011",
        "address": "Pelicano",
        "country": "Spain",
        "city": "Coruña",
        "zip": "15009",
        "identity_number": "33333333V",
    },
}


class ClientTest(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_user_is_created_when_right_parameters_are_specified(self):
        CLIENT_DATA = {
            "first_name": "test_client",
            "last_name": "test_last_name",
            "email": "test_client@email.com",
            "password": "test_pass",
            "profile": {"identity_number": "12345678A", "phone": "555555555"},
        }

        res = self.client.post(BASE_URL, CLIENT_DATA, format="json")
        created_user = User.objects.get(email=CLIENT_DATA.get("email"))
        self.assertEqual(status.HTTP_201_CREATED, res.status_code)
        self.assertEqual(created_user.email, CLIENT_DATA.get("email"))
        self.assertEqual(created_user.first_name, CLIENT_DATA.get("first_name"))
        self.assertEqual(created_user.last_name, CLIENT_DATA.get("last_name"))
        self.assertEqual(
            created_user.profile.identity_number,
            CLIENT_DATA.get("profile").get("identity_number"),
        )

    def test_user_is_not_created_when_no_parameters_is_specified(self):
        CLIENT_DATA = {
            "email": "",
            "first_name": "",
            "password": "",
            "profile": {
                "address": "",
                "country": "",
                "city": "",
                "zip": "",
                "identity_number": "",
            },
        }

        res = self.client.post(BASE_URL, CLIENT_DATA, format="json")
        self.assertEqual(status.HTTP_400_BAD_REQUEST, res.status_code)

    def test_no_superuser_can_be_created_through_api_users(self):
        CLIENT_DATA = {
            "email": "user@gmail.com",
            "first_name": "Firstsuperuser",
            "last_name": "Lastsuperuser",
            "is_superuser": "true",
            "is_owner": "true",
            "password": "superuser",
            "profile": {
                "phone": "671870011",
                "address": "Pelicano",
                "country": "Spain",
                "city": "Coruña",
                "zip": "15009",
                "identity_number": "33333333V",
            },
        }

        res = self.client.post(BASE_URL, CLIENT_DATA, format="json")
        created_user = User.objects.get(email=CLIENT_DATA.get("email"))
        self.assertEqual(status.HTTP_201_CREATED, res.status_code)
        self.assertEqual(created_user.is_superuser, False)
        self.assertEqual(created_user.is_owner, False)

    def test_authenticated_user_cant_access_information_from_regular_user(self):
        CLIENT_DATA1 = {
            "email": "user11@gmail.com",
            "first_name": "First",
            "last_name": "Lasts",
            "password": "superuser",
            "profile": {
                "phone": "671870011",
                "address": "Pelicano",
                "country": "Spain",
                "city": "Coruña",
                "zip": "15009",
                "identity_number": "33333333V",
            },
        }

        authenticated_user = User.objects.create_user(**CLIENT_DATA1)
        self.client.force_authenticate(authenticated_user)
        regular_user = User.objects.create_user(**REGULARUSER_DATA)
        res = self.client.get(BASE_URL + str(regular_user.id) + "/", format="json")
        self.assertEqual(status.HTTP_403_FORBIDDEN, res.status_code)

    def test_signed_in_superuser_can_access_all_information(self):
        SUPERUSER_DATA = {
            "email": "user11@gmail.com",
            "first_name": "First",
            "last_name": "Lasts",
            "password": "superuser",
        }

        superuser = User.objects.create_superuser(**SUPERUSER_DATA)
        self.client.force_authenticate(superuser)
        regular_user = User.objects.create_user(**REGULARUSER_DATA)
        res = self.client.get(BASE_URL + str(regular_user.id) + "/", format="json")
        self.assertEqual(status.HTTP_200_OK, res.status_code)
