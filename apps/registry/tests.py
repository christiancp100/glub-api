from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient

from apps.accounts.models import User

REGISTRY_URL = "/api/registry/create-user/"


class RegistryTests(TestCase):
    def setup(self):
        self.client = APIClient()

    def test_create_registry(self):
        USER_DATA = {
            "firstName": "First",
            "lastName": "Last Last",
            "email": "test@client.com",
            "phone": "650234512",
            "identityNumber": "11111122A",
        }
        res = self.client.post(REGISTRY_URL, USER_DATA)
        user = User.objects.get(email=USER_DATA.get("email"))
        self.assertEqual(user.first_name, USER_DATA.get("firstName"))
        self.assertEqual(user.last_name, USER_DATA.get("lastName"))
        self.assertEqual(user.id_number, USER_DATA.get("identity_number"))
        self.assertEqual(user.id_number, USER_DATA.get("phone"))

        self.assertEqual(res.status_code, status.HTTP_201_CREATED)

    def test_create_duplicated_registry_reuses_information(self):
        pass

    def test_retrieve_user_id_given_qr(self):
        pass
