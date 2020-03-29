from django.test import TestCase
from list.models import Item,List

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
        



