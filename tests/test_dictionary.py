import unittest
from lexpp.dictionary import LexicalDictionary


class TestDictionary(unittest.TestCase):
    def test_version_info(self):
        test_info = (1, 2, 3)
        d = LexicalDictionary(test_info)
        
        self.assertEqual(test_info, d.get_version_info())