from django.test import TestCase
from rest_framework.test import APIClient


class TestUser(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_user_is_created_successfully_with_the_right_data(self):
        pass

    def test_user_receives_token_when_logs_in(self):
        pass

    def test_user_doesnt_log_in_with_wrong_credentials(self):
        pass

    def test_user_receives_refresh_token(self):
        pass
