import datetime

from django.test import TestCase
from rest_framework.test import APIClient

from apps.accounts.models import User
from apps.bars.models import Bar
from apps.events.models import Event


def sample_owner(email="owner@test.com", password="password_test"):
    return User.objects.create_owner({"email": email, "password": password})


def sample_bar(owner, name="Test Bar"):
    return Bar.objects.create(name=name, owner=owner)


EVENTS_URL = "/api/events/"


class PrivateEventTest(TestCase):
    def setUp(self):
        self.user = sample_owner()
        self.bar = sample_bar(owner=self.user)
        self.client = APIClient()
        self.client.force_authenticate(self.user)

    def test_when_owner_creates_event_for_their_bar_it_is_created_successfully(self):
        EVENT_DATA = {
            "name": "Test Party",
            "description": "Test Party Description",
            "start_date": "2021-08-19T22:00:00Z",
            "finish_date": "2021-08-19T22:00:00Z",
            "capacity": 200,
            "is_active": True,
            "created_by": self.user.id,
            "bar": self.bar.id,
        }

        self.client.post(EVENTS_URL, EVENT_DATA)

        event = Event.objects.get(name=EVENT_DATA.get("name"))

        self.assertEqual(EVENT_DATA.get("description"), event.description)
        self.assertEqual(EVENT_DATA.get("capacity"), event.capacity)
        self.assertEqual(EVENT_DATA.get("is_active"), event.is_active)
        self.assertEqual(EVENT_DATA.get("bar"), event.bar.id)
        self.assertEqual(EVENT_DATA.get("created_by"), event.created_by.id)

    def test_when_owner_creates_event_for_not_owned_bar_it_throws_unauthorized(self):
        pass

    def test_when_admin_creates_event_for_any_bar_it_is_created_successfully(self):
        pass

    def test_when_start_data_is_after_finish_date_is_throws_validation_error(self):
        pass
