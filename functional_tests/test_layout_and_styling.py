from selenium.webdriver.common.keys import Keys
from functional_tests.base import FunctionalTest


class LayoutAndStylingTest(FunctionalTest):

    def test_layout_and_styling(self):
        #Edith goes to homepage
        self.browser.get(self.live_server_url)
        self.browser.set_window_size(1024, 768)

        # she notices the input is nicely centered
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertAlmostEqual(
            inputbox.location['x'] + inputbox.size['width'] / 2,
            512,
            delta=10,
        )

        # she enter a new todo task and notices the inputbox also at the center
        inputbox.send_keys('a new todo list item')
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: a new todo list item')
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertAlmostEqual(
            inputbox.location['x'] + inputbox.size['width'] / 2,
            512,
            delta=10,
        )