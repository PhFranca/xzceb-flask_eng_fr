"""
Unit tests for the translator module.
"""

import unittest
from .translator import english_to_french, french_to_english

class TestTranslator(unittest.TestCase):
    """
    Test cases for the translator module.
    """

    def test_translation_hello(self):
        """
        Test translation from English to French for 'Hello'.
        """
        self.assertEqual(english_to_french('hello').lower(), 'bonjour')
        self.assertNotEqual(english_to_french('hello').lower(), 'kello')

    def test_translation_bonjour(self):
        """
        Test translation from French to English for 'Bonjour'.
        """
        self.assertEqual(french_to_english('bonjour').lower(), 'hello')
        self.assertNotEqual(french_to_english('bonjour').lower(), 'bonjuar')

if __name__ == '__main__':
    unittest.main()