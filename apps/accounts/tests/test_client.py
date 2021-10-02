from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from apps.accounts.models.user import User
from apps.accounts.serializers import UserSerializer

BASE_URL = "/api/users/"


class ClientTest(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_user_is_created_when_right_parameters_are_specified(self):
        CLIENT_DATA = {
            'first_name': "test_client",
            'last_name': "test_last_name",
            'email': "test_client@email.com",
            'password': 'test_pass',
            'profile': {
                'identity_number': "12345678A",
                'phone':"555555555"
            }
        }

        res = self.client.post(BASE_URL, CLIENT_DATA, format="json")
        created_user = User.objects.get(email=CLIENT_DATA.get("email"))
        self.assertEqual(status.HTTP_201_CREATED, res.status_code)
        self.assertEqual(created_user.email, CLIENT_DATA.get('email'))
        self.assertEqual(created_user.first_name, CLIENT_DATA.get('first_name'))
        self.assertEqual(created_user.last_name, CLIENT_DATA.get('last_name'))
        self.assertEqual(created_user.profile.identity_number, CLIENT_DATA.get("profile").get("identity_number"))
