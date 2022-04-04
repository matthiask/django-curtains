from django.conf import settings
from django.contrib.auth.models import User
from django.test import Client, TestCase
from django.test.utils import override_settings

from curtains.only_staff import convert_list_to_re


@override_settings(
    MIDDLEWARE=settings.MIDDLEWARE + ["curtains.middleware.only_staff"],
)
class OnlyStaff(TestCase):
    def test_middleware(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 403)

        response = self.client.get("/admin/")
        self.assertEqual(response.status_code, 302)

        response = self.client.get("/admin/login/")
        self.assertEqual(response.status_code, 200)

        response = self.client.get("/accounts/")
        self.assertEqual(response.status_code, 404)

    def test_authenticated(self):
        user = User.objects.create_superuser("test", "t@example.com", "test")
        client = Client()
        client.force_login(user)

        response = client.get("/")
        self.assertEqual(response.status_code, 404)

        response = client.get("/admin/")
        self.assertEqual(response.status_code, 200)

    def test_convert_list_to_re(self):
        self.assertEqual(convert_list_to_re("bla"), "bla")
        self.assertEqual(convert_list_to_re(("bla",)), "^bla")
        self.assertEqual(convert_list_to_re(("bla", "blu")), "^bla|^blu")

    @override_settings(
        ONLY_STAFF_EXEMPT=r"^/answer/",
    )
    def test_exempt_re(self):
        response = self.client.get("/answer/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content, b"42")

        response = self.client.get("/other/")
        self.assertEqual(response.status_code, 403)

    @override_settings(
        ONLY_STAFF_EXEMPT=["/answer/"],
    )
    def test_exempt_list(self):
        response = self.client.get("/answer/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content, b"42")

        response = self.client.get("/other/")
        self.assertEqual(response.status_code, 403)
