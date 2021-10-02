from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from apps.bars.models import Bar
from apps.bars.serializers import BarSerializer

BARS_URL = "/api/bars/"


def sample_owner(email="test@company.com", password="test_pass"):
    """ Creates a sample owner to test """
    return get_user_model().objects.create_owner(email, password)


def sample_admin(email="test@company.com", password="test_pass"):
    """ Creates a sample owner to test """
    return get_user_model().objects.create_superuser(email, password)


def sample_client(email="client@mail.com", password="test_pass"):
    """ Creates a sample client to test """
    return get_user_model().objects.create_user(email, password)


class PublicBarTests(TestCase):

    def setUp(self):
        self.client = APIClient()

    def test_login_not_required_to_list(self):
        res = self.client.get(BARS_URL)
        self.assertEquals(res.status_code, status.HTTP_200_OK)

    def test_retrieve_bars(self):
        Bar.objects.create(name="TestBar1", owner=sample_owner("test@company.com"))
        Bar.objects.create(name="TestBar2", owner=sample_owner("competence@company.com"))
        bars = Bar.objects.all().order_by('-name')
        serializer = BarSerializer(bars, many=True)

        res = self.client.get(BARS_URL)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)


class PrivateBarTests(TestCase):

    def setUp(self):
        self.user = sample_owner()
        self.client = APIClient()
        self.client.force_authenticate(self.user)

    def test_create_bar_with_name_successful(self):
        BAR_DATA = {
            'name': 'Anonymous Bar',
            'address': '123 Main St',
            'capacity': 300
        }
        res = self.client.post(BARS_URL, BAR_DATA)

        bar = Bar.objects.get(name=BAR_DATA.get('name'))
        self.assertTrue(Bar.objects.filter(name=BAR_DATA.get('name')).exists())
        self.assertEqual(res.data.get('name'), bar.name)

    def test_client_cannot_create_bar(self):
        BAR_DATA = {
            'name': 'Anonymous Bar',
            'address': '123 Main St',
            'capacity': 300
        }
        self.user.is_owner = False

        res = self.client.post(BARS_URL, BAR_DATA)

        self.assertEqual(res.status_code, status.HTTP_403_FORBIDDEN)

    def test_admin_can_create_bar(self):
        BAR_DATA = {
            'name': 'Anonymous Bar',
            'address': '123 Main St',
            'capacity': 300
        }
        self.user.is_superuser = True
        owner = sample_owner("another@owner.com", "test_pass")
        BAR_DATA.update({'owner': owner.id})

        res = self.client.post(BARS_URL, BAR_DATA)

        self.assertEqual(res.data.get('owner').get('id'), owner.id)

    def test_admin_cannot_create_bar_when_missing_owner(self):
        BAR_DATA = {
            'name': 'Anonymous Bar',
            'address': '123 Main St',
            'capacity': 300
        }
        self.user.is_superuser = True

        res = self.client.post(BARS_URL, BAR_DATA)

        self.assertEqual(res.status_code, status.HTTP_404_NOT_FOUND)

    def test_owner_can_update_bar(self):
        BAR_DATA = {
            'name': 'Anonymous Bar',
            'address': '123 Main St',
            'capacity': 300
        }
        bar = Bar.objects.create(owner=self.user, **BAR_DATA)
        BAR_DATA.update({'name': 'Aristo Bar'})
        url = BARS_URL + str(bar.id) + "/"

        self.client.put(url, BAR_DATA)

        updated_bar = Bar.objects.get(id=bar.id)
        self.assertEqual(updated_bar.name, BAR_DATA.get('name'))

    def test_owner_cannot_update_other_owner_bar(self):
        BAR_DATA = {
            'name': 'Anonymous Bar',
            'address': '123 Main St',
            'capacity': 300
        }
        another_owner = sample_owner("another_owner", "test_pass")
        bar = Bar.objects.create(owner=another_owner, **BAR_DATA)
        BAR_DATA.update({'name': 'Aristo Bar'})
        url = BARS_URL + str(bar.id) + "/"

        res = self.client.put(url, BAR_DATA)

        self.assertEqual(res.status_code, status.HTTP_403_FORBIDDEN)

    def test_admin_can_update_bar(self):
        pass

    def test_owner_can_list_their_bars(self):
        # TODO
        pass
