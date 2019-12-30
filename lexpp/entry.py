#coding:utf-8

class Entry:

    def __init__(self, surface: str, group_id: int):
        self.surface = surface
        self.group_id = group_id

        self.declinable_flg = False
        self.expand_controll_flg = False

        self.lex_id = 0
        self.form_type = 0
        self.abbr_info = 0
        self.variant_info = 0
        self.category = ""

    def __repr__(self):
        return ','.join([str(x) for x in [self.surface, self.group_id, self.declinable_flg, self.expand_controll_flg, self.lex_id, self.form_type, self.abbr_info, self.variant_info, self.category]])
