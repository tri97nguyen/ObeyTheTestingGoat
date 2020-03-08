from django.test import TestCase
from django.urls import resolve
from list.views import home_page
# Create your tests here.

# this is second line
class HomePageTest(TestCase):
    def test_root_url_resolves_to_homepage_view(self):
        found = resolve('/')
        self.assertEqual(found.func,home_page)