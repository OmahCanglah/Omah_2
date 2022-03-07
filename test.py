import unittest
from is_pal import is_palindrome

class TestStringMethods(unittest.TestCase):

    def test_foo(self):
        self.assertFalse(is_palindrome('foo'))

    def test_foo(self):
        self.assertTrue(is_palindrome('noon'))

