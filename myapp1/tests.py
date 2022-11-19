from django.test import TestCase, Client
from .views import index_page


class StatisticsTests(TestCase):
    def setUp(self) -> None:
        self.client = Client()

    def test_index_page_GET_is_working(self):
        response = self.client.get(path='')
        self.assertEqual(response.status_code, 200)

    def test_index_page_POST_is_working(self):
        response = self.client.post(path='', data={'SendMeText': "hello"})
        self.assertEqual(response.status_code, 200)

    def test_index_page_returned_headers(self):
        response = self.client.post(path='', data={'SendMeText': "hello"})
        self.assertEqual(response.headers.get('Content-Type'), 'text/html; charset=utf-8')

    def test_index_page_changes_brackets(self):
        response = self.client.post(path='', data={'SendMeText': '"hello"'})
        html_answer = ''.join([r.decode() for r in response])
        self.assertEqual(html_answer, '<h1>Ты ввел: "hello"</h1><h1>Отредактированный текст: «hello»</h1>')
