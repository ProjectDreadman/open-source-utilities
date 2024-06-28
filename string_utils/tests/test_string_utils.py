import unittest
from string_utils import reverse_string, is_palindrome

class TestStringUtils(unittest.TestCase):
    def test_reverse_string(self):
        self.assertEqual(reverse_string("hello"), "olleh")
        self.assertEqual(reverse_string("world"), "dlrow")

    def test_is_palindrome(self):
        self.assertTrue(is_palindrome("racecar"))
        self.assertTrue(is_palindrome("A man a plan a canal Panama"))
        self.assertFalse(is_palindrome("hello"))

if __name__ == "__main__":
    unittest.main()
