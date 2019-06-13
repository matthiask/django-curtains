from django.conf import settings
from django.test import TestCase
from django.test.utils import override_settings


@override_settings(
    MIDDLEWARE=["curtains.middleware.basic_auth"] + settings.MIDDLEWARE,
    BASIC_AUTH_CREDENTIALS=["user", "pw"],
)
class BasicAuth(TestCase):
    def test_middleware(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 401)

        response = self.client.get("/", HTTP_AUTHORIZATION="bla bla")
        self.assertEqual(response.status_code, 401)

        response = self.client.get("/", HTTP_AUTHORIZATION="Basic 01234567")
        self.assertEqual(response.status_code, 401)

        response = self.client.get("/", HTTP_AUTHORIZATION="Basic dXNlcjpwdw==")
        self.assertEqual(response.status_code, 404)
