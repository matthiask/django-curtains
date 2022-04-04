from django.conf import settings
from django.test import TestCase
from django.test.utils import override_settings


@override_settings(
    MIDDLEWARE=settings.MIDDLEWARE + ["curtains.middleware.ip_networks_only"]
)
class IPNetworksOnly(TestCase):
    def test_middleware(self):
        response = self.client.get("/", HTTP_REMOTE_ADDR="127.0.0.1")
        self.assertEqual(response.status_code, 404)

        response = self.client.get("/", HTTP_X_FORWARDED_FOR="1.1.1.1")
        self.assertEqual(response.status_code, 403)

    @override_settings(
        IP_NETWORKS_EXEMPT=r"^/answer/",
    )
    def test_exempt_re(self):
        response = self.client.get("/answer/", HTTP_X_FORWARDED_FOR="1.1.1.1")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content, b"42")

        response = self.client.get("/other/", HTTP_X_FORWARDED_FOR="1.1.1.1")
        self.assertEqual(response.status_code, 403)
