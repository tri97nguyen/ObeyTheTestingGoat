from django.test import TestCase
from django.urls import resolve
from django.http import HttpRequest
from list.views import home_page
from django.template.loader import render_to_string
from list.models import Item

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

    def test_saving_and_retrieving_items(self):
        first_item = Item()
        first_item.text = 'the first (ever) list item'
        first_item.save()

        second_item = Item()
        second_item.text = 'item second'
        second_item.save()
        
        saved_items = Item.objects.all()
        self.assertEqual(saved_items.count(),2)
        
        first_saved_item = saved_items[0]
        second_saved_item = saved_items[1]
        self.assertEqual(first_saved_item.text,first_item.text)
        self.assertEqual(second_saved_item.text,second_item.text)
        
        