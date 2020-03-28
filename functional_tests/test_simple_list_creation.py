from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from functional_tests.base import FunctionalTest


# class NewVisitorTest(LiveServerTestCase):
class NewVisitorTest(FunctionalTest):

    def test_visitor_visit_page(self):
        #user go to the website
        self.browser.get(self.live_server_url)
        
        #user see the title as to-do
        self.assertIn("To-Do",self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do',header_text)

        # she is invited to enter the list immediately
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(inputbox.get_attribute('placeholder'),'Enter a to-do item')

        inputbox.send_keys('Buy peacock feathers')
        # When she hits enter, the page updates, and now the page lists
        # "1: Buy peacock feathers" as an item in a to-do list table
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: Buy peacock feathers')
        
        # There is still a text box inviting her to add another item. She
        # ​# enters "Use peacock feathers to make a fly" (Edith is very
        # ​# methodical)
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Use peacock feathers to make a fly')
        inputbox.send_keys(Keys.ENTER)
        
        
        self.wait_for_row_in_list_table('2: Use peacock feathers to make a fly')

        self.fail('finish the test')

    def test_multiple_users_can_start_lists_at_different_urls(self):
        # Edith opens browswer and go to her dedicated website
        self.browser.get(self.live_server_url)
        
        # Edith start endtering her first todo
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys("Buy peacock feathers")
        inputbox.send_keys(Keys.ENTER)


        self.wait_for_row_in_list_table('1: Buy peacock feathers')
        # Edith sees her unique URL
        self.assertRegex(self.browser.current_url, '/list/.+',f'current url is {self.browser.current_url}')
        edith_url = self.browser.current_url
        
        
        # Edith start entering her second todo
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys("Use peacock feathers to make a fly")
        inputbox.send_keys(Keys.ENTER)

        self.wait_for_row_in_list_table("2: Use peacock feathers to make a fly")
        # After seeing the todos, she close the browser and goes to bed
        self.browser.quit()

        ## We use a new browser to make sure no information of Edith could
        ## come into Francis' session via cookies,etc
        # Now a new user, Francis, visit the website
        # Francis open browser and enter site url
        self.browser = webdriver.Firefox()
        self.browser.get(self.live_server_url)
        
        page_text = self.browser.find_element_by_tag_name('body').text

        # The website must not contain Edith saved todo list
        self.assertNotIn('Buy peacock feathers',page_text)
        self.assertNotIn('Use peacock feathers to make a fly',page_text)

        # After seeing his page is blank, Francis start entering todo tasks
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('buy milk')
        inputbox.send_keys(Keys.ENTER)

        # Francis hits enter and sees todo tasks appear
        self.wait_for_row_in_list_table('1: buy milk')
        # Francis sees his unique url
        self.assertRegex(self.browser.current_url, '/list/.+')
        # Francis url is unique form Edith
        francis_url = self.browser.current_url
        self.assertNotEqual(edith_url, francis_url)

