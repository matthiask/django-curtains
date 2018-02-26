from __future__ import absolute_import, unicode_literals

from django.test import TestCase
from django.test.utils import override_settings


@override_settings(
)
class OnlyStaff(TestCase):
    def test_tag(self):
        response = self.client.get('/')
        self.assertEqual(
            response.status_code,
            403,
        )

        response = self.client.get('/admin/')
        self.assertEqual(
            response.status_code,
            302,
        )

        response = self.client.get('/admin/login/')
        self.assertEqual(
            response.status_code,
            200,
        )

        response = self.client.get('/accounts/')
        self.assertEqual(
            response.status_code,
            404,
        )
