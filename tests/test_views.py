from django.test import TestCase
from django.test import Client

class TypeformViewTest(TestCase):
    def test_view(self):
        c = Client()
        response = c.get('/testform/')
        self.assertEqual(response.status_code, 200)
