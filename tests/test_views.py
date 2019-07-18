from django.test import SimpleTestCase
from django.test import Client

class TypeformViewTest(SimpleTestCase):
    def test_view(self):
        c = Client()
        response = c.get('/testform/')
        self.assertEqual(response.status_code, 200)
