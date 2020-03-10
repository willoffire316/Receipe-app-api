from django.test import TestCase
from app.calc import  add,sub

class calcTest(TestCase):
    
    def test_add_numbers(self):
        """ Test That add two Numbers Together"""
        self.assertEqual(add(3,7), 10)


    def test_subtract_numbers(self):
        """ Test that two numbers subtract """
        self.assertEqual(sub(5,3), 2)

