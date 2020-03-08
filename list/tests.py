from django.test import TestCase
from django.urls import resolve
from django.http import HttpRequest
from list.views import home_page
# Create your tests here.

# this is second line
class HomePageTest(TestCase):
    def test_root_url_resolves_to_homepage_view(self):
        found = resolve('/')
        self.assertEqual(found.func,home_page)

    def test_home_page_resolve_return_html(self):
        request = HttpRequest()
        response = home_page(request)
        html = response.content.decode('utf8')
        self.assertTrue(html.startswith('<html>'))
        self.assertIn('<title>To-Do lists</title>',html)
        self.assertTrue(html.endswith('</html>'))
