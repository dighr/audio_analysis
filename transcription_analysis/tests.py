from django.test import TestCase
from django.test import Client


class ResponseTestCase(TestCase):
    def test_text_analysis_path_retreives_correct_code(self):
        c = Client()
        response = c.get('/text/analyze?text=hello world&method=google')
        self.assertEqual(response.status_code, 200)

    def test_api_key_retrieves_correct_values(self):
        pass

