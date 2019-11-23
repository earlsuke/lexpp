import unittest
import pkg_resources

from lexpp.lexpp import Lexpp
from lexpp.entry import Entry
from lexpp.dictionary import LexicalDictionary


class TestLexpp(unittest.TestCase):

    def test_functionallity(self):
        """
        tests for basic functionality
        in thie case, the test model ("lexpp/tests/test.dict") is used.
        """

        pp = Lexpp(external_dict=pkg_resources.resource_filename("lexpp", "tests/test.dict"))

        test_word = "キャプテン"
        entries = list(pp.lookup(test_word))

        self.assertEqual(len(entries), 4)

        for e in entries:
            self.assertEqual(type(e), Entry)
            rep = pp.get_representative_form(e)
            self.assertEqual(rep, test_word)

    def test_functionallity_for_simple_word(self):
        """
        operation validation : On the test model, a word "ソート" has 8 synonyms.
        """

        """
        from synonyms.txt

        000437,1,0,1,0,0,0,(IT),ソート,,
        000437,1,0,1,0,0,1,(IT),sort,,
        000437,1,0,2,0,0,0,(IT),並び替え,,
        000437,1,0,2,0,0,2,(IT),並び換え,,
        000437,1,0,2,0,0,2,(IT),並びかえ,,
        000437,2,0,3,0,0,0,(IT),並び替える,,
        000437,2,0,3,0,0,2,(IT),並び換える,,
        000437,2,0,3,0,0,2,(IT),並びかえる,,
        """

        test_word = "ソート"

        pp = Lexpp(external_dict=pkg_resources.resource_filename("lexpp", "tests/test.dict"))
        ent = list(pp.lookup(test_word))

        self.assertEqual(len(ent), 1)

        synset = list(pp.get_synset(ent[0]))

        self.assertEqual(len(synset), 8)

    def test_default_model(self):
        """
        for default model loading
        """

        try:
            pp = Lexpp()
        except Exception:
            self.fail("initialize was failed")

    def test_custom_model(self):
        """
        for custom model loading
        """

        try:
            pp = Lexpp(external_dict=pkg_resources.resource_filename("lexpp", "tests/test.dict"))
        except Exception:
            self.fail("init was failed")
 
    def test_dict_with_invalid_version(self):
        """
        when the given dictionary was built with invalid version, Lexpp() must raise an FileNotFoundError.
        """

        invalid_version_info = (-1, -1, -1)
        d = LexicalDictionary(invalid_version_info)

        with self.assertRaises(FileNotFoundError):
            lp = Lexpp(external_dict=d)


if __name__ == '__main__':
    unittest.main()
