import unittest

from palindromos import is_palindrome

class TestIsPalindrome(unittest.TestCase):
    def test_with_a(self):
        value = "a"
        result = is_palindrome(value)
        self.assertTrue(result)
        
    def test_with_ala(self):
        value = "ala"
        result = is_palindrome(value)
        self.assertTrue(result)
        
    def test_with_neuquen(self):
        value = "neuquen"
        result = is_palindrome(value)
        self.assertTrue(result)
        
    def test_with_hola(self):
        value = "hola"
        result = is_palindrome(value)
        self.assertFalse(result)
        
if __name__ == '__main__':
    unittest.main()