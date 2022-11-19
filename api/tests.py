from rest_framework.test import APITestCase


class StatisticsTests(APITestCase):
    def test_api(self):
        url = 'https://127.0.0.1:8000/api/abc'
        response = self.client.get(url)
        self.assertEqual(response.data, {"symbol_count": {"a": 1, "b": 1, "c": 1}, "str_len": 3})
