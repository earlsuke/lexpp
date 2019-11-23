import unittest
from lexpp.entry import Entry
from lexpp.dict_builder import DictBuilder


class TestDictBuilder(unittest.TestCase):

    representive_entry = None
    not_representive_entry = None

    @classmethod
    def setUpClass(cls):
        cls.representive_entry = Entry("代表表記", 1)
        cls.representive_entry.variant_info = 0
        cls.representive_entry.form_type = 0
        cls.representive_entry.abbr_info = 0

        cls.not_representive_entry = Entry("代表表記ではない", 1)
        cls.not_representive_entry.variant_info = 1
        cls.not_representive_entry.form_type = 1
        cls.not_representive_entry.abbr_info = 2

    def test_is_representive(self):
        self.assertEqual(True, DictBuilder.is_representive(TestDictBuilder.representive_entry))
        self.assertEqual(False, DictBuilder.is_representive(TestDictBuilder.not_representive_entry))