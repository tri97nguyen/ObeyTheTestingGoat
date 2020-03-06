from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
    def tearDown(self):
        self.browser.quit()
    def test_visitor_visit_page(self):
        #user go to the website
        self.browser.get('http://localhost:8000')
        #user see the title as to-do
        self.assertIn("to-do",self.browser.title)
        self.fail('finish the test')
        #user enter 
        

if __name__ == '__main__':
    unittest.main()