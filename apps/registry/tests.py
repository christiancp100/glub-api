from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient
from apps.accounts.models import User
from .models import Registry

REGISTRY_URL = "/api/registry/"


class RegistryTests(TestCase):
    def setup(self):
        self.client = APIClient()

    def test_create_registry(self):
        USER_DATA = {
            'idNumber': "459456458W",
            'firstName': "First",
            'lastName': "Last Last",
            'phone': 650234512
        }
        res = self.client.post(REGISTRY_URL, USER_DATA)

        user = User.objects.get(phone=USER_DATA.get('phone'))
        self.assertEqual(user.first_name, USER_DATA.get('firstName'))
        self.assertEqual(user.last_name, USER_DATA.get('lastName'))
        self.assertEqual(user.id_number, USER_DATA.get('idNumber'))

        self.assertEqual(res.status_code, status.HTTP_201_CREATED)

    def test_create_duplicated_registry_reuses_information(self):
        pass

    def test_retrieve_user_id_given_qr(self):
        pass
