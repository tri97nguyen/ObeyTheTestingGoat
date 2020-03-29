from django.test import TestCase
from django.urls import resolve
from django.http import HttpRequest,HttpResponse
from list.views import home_page
from django.template.loader import render_to_string
from list.models import Item,List

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


class ListViewTest(TestCase):
    def test_POST_request_submit_to_correct_list(self):
        list_ = List.objects.create()
        response = self.client.get(f'/list/{list_.id}/')
        self.assertEqual(response.context['list'],list_)


    def test_use_list_template(self):
        list_ = List.objects.create()

        response = self.client.get(f'/list/{list_.id}/')
        self.assertTemplateUsed(response,'list.html')

    def test_display_items_on_that_list(self):
        list1 = List.objects.create()
        item1_list1 = Item.objects.create(text='item1 list1',listy = list1)
        list2 = List.objects.create()
        item2_list2 = Item.objects.create(text='item2 list2',listy = list2)

        response = self.client.get(f'/list/{list1.id}/')
        self.assertContains(response,'item1 list1')
        self.assertNotContains(response, 'item2 list2')

    def test_template_display_multiple_list_item(self):
        list_ = List.objects.create()
        Item.objects.create(text='first item',listy = list_)
        Item.objects.create(text='second item', listy=list_)

        response = self.client.get(f'/list/{list_.id}/')
        html = response.content.decode()
        self.assertContains(response, 'first item')
        self.assertContains(response, 'second item')

        self.assertIn('first item', html)
        self.assertIn('second item', html)

    def test_list_template_is_different_from_home_template(self):
        list_ = List.objects.create()
        listResponse = self.client.get(f'/list/{list_.id}/')
        self.assertTemplateUsed(listResponse,'list.html')

class NewItemTest(TestCase):
    # def test_submitting_item_in_a_list_page_would_redirect_back_to_that_list_page(self):
    #     list_ = List.objects.create()
    #     context = {'item_text': 'new list item'}
    #     # response = self.client.post(f'/list/2/new-item/',context)
    #     response = self.client.post(f'/list/{list_.id}/newitem/',{'item_text':'new list item'})
        
    #     self.assertRedirects(response,f'/list/{list_.id}/')
    #     html = response.content.decode()
    #     print('iam here')
    #     print(html)

    def test_can_save_a_POST_request_to_an_existing_list(self):
        other_list = List.objects.create()
        correct_list = List.objects.create()
        data = {'item_text':'a new list item'}
        
        self.client.post(f'/list/{correct_list.id}/add_item',data)

        item = Item.objects.first()
        self.assertEqual(item.listy, correct_list)
        self.assertEqual(item.text, 'a new list item')

    def test_redirects_to_list_view(self):
        other_list = List.objects.create()
        list_ = List.objects.create()

        response = self.client.post(f'/list/{list_.id}/add_item',{'item_text':'a new list item'})
        self.assertRedirects(response, f'/list/{list_.id}/')

        response =self.client.get(f'/list/{list_.id}/')
        self.assertContains(response, 'a new list item')
        



        
class NewListTest(TestCase):
    def test_can_save_a_POST_request(self):
        data = {'item_text':'a new list item'}
        self.client.post('/list/new',data)

        self.assertEqual(Item.objects.all().count(),1)
        self.assertEqual(Item.objects.all().first().text,'a new list item')

    def test_redirect_after_POST(self):
        response = self.client.post('/list/new',{'item_text':'a new list item'})
        list_ = List.objects.first()
        self.assertRedirects(response, f'/list/{list_.id}/')
        
        # self.assertEqual(response['location'], f'/list/{list_.id}/')
        # self.assertEqual(response.status_code,301)
