from django.test import TestCase

# Create your tests here.

# this is second line
class SmokeTest(TestCase):
    def test_bad_maths(self):
        self.assertEqual(1+1,3)