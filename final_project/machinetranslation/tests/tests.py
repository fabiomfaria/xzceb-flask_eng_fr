import unittest

from translator import english_to_french, french_to_english

class TestEnglishToFrench(unittest.TestCase): 
    def test1(self): 
        self.assertNotEqual(english_to_french('yes'), 'Oui')
        self.assertNotEqual(english_to_french('Hello'), 'Bonjour')

class TestFrenchToEnglish(unittest.TestCase): 
    def test1(self): 
        self.assertNotEqual(french_to_english('Oui'), 'Oui')
        self.assertNotEqual(french_to_english('Bonjour'), 'Hello')
   
unittest.main()