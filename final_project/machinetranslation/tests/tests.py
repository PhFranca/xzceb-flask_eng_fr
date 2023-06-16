"""
Unit tests for the translator module.
"""

import unittest

class TestTranslator(unittest.TestCase):
    """
    Test cases for the translator module.
    """

    def test_translation_hello(self):
        """
        Test translation from English to French for 'Hello'.
        """
        self.assertEqual(translator.english_to_french('Hello'), 'Bonjour')
        self.assertNotEqual(translator.english_to_french('Hello'), 'Kello')

    def test_translation_bonjour(self):
        """
        Test translation from French to English for 'Bonjour'.
        """
        self.assertEqual(translator.french_to_english('Bonjour'), 'Hello')
        self.assertNotEqual(translator.french_to_english('Bonjour'), 'Bonjuar')

if __name__ == '__main__':
    unittest.main()
