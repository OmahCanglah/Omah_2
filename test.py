import unittest
from is_pal import is_palindrome

class TestStringMethods(unittest.TestCase):

    def test_foo(self):
        self.assertFalse(is_palindrome('foo'))

    def test_noon(self):
        self.assertTrue(is_palindrome('noon'))

    def test_i(self):
        self.assertTrue(is_palindrome('i'))

    def test_redivider(self):
        self.assertTrue(is_palindrome('redivider'))

    def test_coooooooooooooooc(self):
        self.assertTrue(is_palindrome('coooooooooooooooc'))

    def test_did(self):
        self.assertTrue(is_palindrome('did'))
