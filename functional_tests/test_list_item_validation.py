from selenium.webdriver.common.keys import Keys
from unittest import skip
from functional_tests.base import FunctionalTest

class ItemValidationTest(FunctionalTest):

 
    
    def test_cannot_add_empty_list_items(self):
        # Edith goes to the home page and accidentally tries to submit
        # an empty list item. She hits Enter on the empty input box
        self.browser.get(self.live_server_url)
        self.browser.find_element_by_id('id_new_item').send_keys(Keys.ENTER)
        # The home page refreshes, and there is an error message saying
        # that list items cannot be blank
        
        # html_body = self.browser.page_source
        # self.assertIn('list items cannot be blank',html_body)
        self.wait_for(lambda: self.assertEqual(
            self.browser.find_element_by_css_selector('.has-error').text,
            "You can't have an empty list item",
        ))
        
        # She tries again with some text for the item, which now works
        self.browser.find_element_by_id('id_new_item').send_keys('Buy Milk')
        self.browser.find_element_by_id('id_new_item').send_keys(Keys.ENTER)
        self.wait_for(lambda: self.assertIn('Buy Milk',self.browser.page_source))
        # Perversely, she now decides to submit a second blank list item
        self.browser.find_element_by_id('id_new_item').send_keys(Keys.ENTER)
        # She receives a similar warning on the list page
        self.wait_for(lambda: self.assertEqual(
            self.browser.find_element_by_css_selector('.has-error').text,
            "You can't have an empty list item",
        ))
        # print('I am safe')
        # And she can correct it by filling some text in
        self.browser.find_element_by_id('id_new_item').send_keys('Make Tea')
        self.browser.find_element_by_id('id_new_item').send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: Buy Milk')
        self.wait_for_row_in_list_table('2: Make Tea')
        self.fail('write me!')

        
# if __name__ == '__main__':
#     unittest.main()
