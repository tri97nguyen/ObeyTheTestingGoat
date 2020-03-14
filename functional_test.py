from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
import time


class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
    def tearDown(self):
        self.browser.quit()
    def check_task_in_table(self, row_text):
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row.text for row in rows])
    def test_visitor_visit_page(self):
        #user go to the website
        self.browser.get('http://localhost:8000')
        #user see the title as to-do
        self.assertIn("To-Do",self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do',header_text)

        # she is invited to enter the list immediately
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(inputbox.get_attribute('placeholder'),'Enter a to-do item')

        inputbox.send_keys('1: Buy peacock feathers')
        # When she hits enter, the page updates, and now the page lists
        # "1: Buy peacock feathers" as an item in a to-do list table
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)
        self.check_task_in_table('1: Buy peacock feathers')
        # There is still a text box inviting her to add another item. She
        # ​# enters "Use peacock feathers to make a fly" (Edith is very
        # ​# methodical)
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('2: Use peacock feathers to make a fly')
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)
        self.check_task_in_table('1: Buy peacock feathers')
        self.check_task_in_table('2: Use peacock feathers to make a fly')

        self.fail('finish the test')
        
if __name__ == '__main__':
    unittest.main()
