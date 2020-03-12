from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
import time


class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
    def tearDown(self):
        self.browser.quit()
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

        # she enter the todo task
        inputbox.send_keys('Buy peacock feathers')
        # when she hits enter, the page stores the task and display it back
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        table = self.browser.find_element_by_name('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertTrue(
            any(row.text == '1: Buy peacock feathers' for row in rows)
        )


        # there is still a text box inviting her to add another item.
        # she enters "use peacock feathers to make a fly"
        
        self.fail('finish the test')

        # the page update again and shows both items on the list
        
    
        
        

if __name__ == '__main__':
    unittest.main()