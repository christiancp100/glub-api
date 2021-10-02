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
            'name': "test_client",
            'email': "test_client@email.com",
            'password': 'test_pass'
        }

        res = self.client.post(BASE_URL, CLIENT_DATA)

        created_user = User.objects.get(email=CLIENT_DATA.get("email"))
        serialized_user = UserSerializer(data=created_user)
        self.assertTrue(serialized_user.is_valid(raise_exception=True))
        self.assertEqual(status.HTTP_201_CREATED, res.status_code)
        self.assertEqual(created_user.email, CLIENT_DATA.get('email'))
        self.assertEqual(created_user.name, CLIENT_DATA.get('name'))
        self.assertEqual(serialized_user.data, res.data)
