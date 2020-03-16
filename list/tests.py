from django.test import TestCase
from django.urls import resolve
from django.http import HttpRequest,HttpResponse
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

    def test_not_save_Item_on_get_request(self):
        response = self.client.get('/')
        self.assertEqual(Item.objects.all().count(),0)
        
    def test_can_save_a_POST_requets(self):
        data = {'item_text': 'A new list item'}
        response = self.client.post('/',data)
        self.assertEqual(Item.objects.all().first().text,'A new list item')

    def test_can_redirect_after_POST_requets(self):
        response = self.client.post('/',{'item_text':'some input'})
        self.assertEqual(response.status_code,302)
        self.assertEqual(response['location'],'/')

    

    def test_template_display_multiple_list_item(self):
        Item.objects.create(text='first item')
        Item.objects.create(text='second item')

        response = self.client.get('/')
        html = response.content.decode()

        self.assertIn('first item',html)
        self.assertIn('second item',html)


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
        
