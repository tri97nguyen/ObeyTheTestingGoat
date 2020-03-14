from django.test import TestCase
from django.urls import resolve
from django.http import HttpRequest
from list.views import home_page
from django.template.loader import render_to_string

from selenium import webdriver

# Create your tests here.
# this is second line
class HomePageTest(TestCase):


    def test_home_page_resolve_return_html(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')
        
    def test_can_save_a_POST_requets(self):
        data = {'item_text': 'A new list item'}
        response = self.client.post('/',data)
        self.assertIn('A new list item',response.content.decode())
        
        