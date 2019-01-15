from django.test import TestCase
from django.test import SimpleTestCase
# Create your tests here.
class SimpleTests(SimpleTestCase):
    def test_index_page(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
    def test_detail_page(self):
        response = self.client.get('/detail/')
        self.assertEqual(response.status_code, 200)
    def test_result_page(self):
        response = self.client.get('/result/')
        self.assertEqual(response.status_code, 200)
