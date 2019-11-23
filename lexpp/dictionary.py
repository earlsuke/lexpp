from typing import Tuple
from collections import defaultdict


class LexicalDictionary:

    def __init__(self, version_info: Tuple[int, int, int]):

        self.category2id = dict()
        self.surface2entry_ids = defaultdict(list)
        self.groupid2synonym_ids = defaultdict(list)
        self.groupid_lexid2representive_form = dict()
        self.entries = []

        self._VERSION_INFO = version_info

    def get_version_info(self) -> Tuple[int, int, int]:
        return self._VERSION_INFO
