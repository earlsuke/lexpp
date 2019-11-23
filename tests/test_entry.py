import unittest
from lexpp.entry import Entry


class TestEntry(unittest.TestCase):

    def test_rpr(self):

        test_surface = "sample"
        test_id = 10

        e = Entry(test_surface, test_id)
        rpr = ','.join([str(x) for x in [e.surface, e.group_id, e.declinable_flg, e.expand_controll_flg, e.lex_id, e.form_type, e.abbr_info, e.variant_info, e.category]])
        self.assertEqual(rpr, str(e))
