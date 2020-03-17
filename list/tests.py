from django.test import TestCase
from django.urls import resolve
from django.http import HttpRequest,HttpResponse
from list.views import home_page
from django.template.loader import render_to_string
from list.models import Item,List

from selenium import webdriver

# Create your tests here.
# this is second line
class ListAndItemModelTest(TestCase):

    def test_save_and_retrieve_item_and_list(self):
        list_ = List()
        list_.save()

        first_item = Item()
        first_item.text = 'the first ever list item'
        first_item.listy = list_
        first_item.save()

        second_item = Item()
        second_item.text = 'the second item'
        second_item.listy = list_
        second_item.save()

        saved_list = List.objects.all()
        
        self.assertIn(list_,saved_list)

        self.assertEqual(first_item, Item.objects.all().first())
        self.assertEqual(Item.objects.all()[0].listy, list_)
        
        self.assertEqual(second_item, Item.objects.all()[1])
        self.assertEqual(second_item.listy, list_)
        



class HomePageTest(TestCase):


    def test_home_page_resolve_return_html(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')

    def test_not_save_Item_on_get_request(self):
        response = self.client.get('/')
        self.assertEqual(Item.objects.all().count(),0)


class ListViewTest(TestCase):

    def test_template_display_multiple_list_item(self):
        list_ = List.objects.create()
        Item.objects.create(text='first item',listy = list_)
        Item.objects.create(text='second item', listy=list_)

        response = self.client.get('/list/unique-list-url-for-each-user')
        html = response.content.decode()
        self.assertContains(response, 'first item')
        self.assertContains(response, 'second item')

        self.assertIn('first item', html)
        self.assertIn('second item', html)

    def test_list_template_is_different_from_home_template(self):
        listResponse = self.client.get('/list/unique-list-url-for-each-user')
        self.assertTemplateUsed(listResponse,'list.html')



        
class NewListTest(TestCase):
    def test_can_save_a_POST_request(self):
        data = {'item_text':'a new list item'}
        self.client.post('/list/new',data)

        self.assertEqual(Item.objects.all().count(),1)
        self.assertEqual(Item.objects.all().first().text,'a new list item')

    def test_redirect_after_POST(self):
        response = self.client.post('/list/new',{})

        self.assertRedirects(response, '/list/unique-list-url-for-each-user')
        # self.assertEqual(response['location'],'/list/unique-list-url-for-each-user')
        # self.assertEqual(response.status_code,302)
