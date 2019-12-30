# coding:utf-8

from typing import Tuple, Dict, List, Set
from pkg_resources import resource_stream
import pickle as pkl

from lexpp.entry import Entry
from lexpp.dictionary import LexicalDictionary

import sys
sys.modules["dictionary"] = LexicalDictionary


class Lexpp:

    __version_info__ = (1, 1, 0)

    def __init__(self, external_dict_path: str = "", external_dict: LexicalDictionary = None):
        # prepare dicts
        self.__resources = None

        if external_dict != None and type(external_dict) == LexicalDictionary:
            # load external model from data
            self.__resources = external_dict

        else:
            if external_dict_path == "":
                # load default model
                with resource_stream('lexpp', 'res/synonyms.dict') as default_model:
                    self.__resources = pkl.load(default_model)

            else:
                # load external model from path
                with open(external_dict_path, mode="rb") as ext:
                    self.__resources = pkl.load(ext)

        if not self._validate_versions():
            raise FileNotFoundError("[Error]the version of loaded dicrionary is not valid")

    def get_version_info(self):
        """
        returns the version info:
        version_info(major, minor, debug)
        """
        return self.__version_info__

    def _validate_versions(self) -> bool:
        """
        confirms the correctness between library and resource
        """
        if self.__resources is None:
            return False

        if Lexpp.__version_info__ != self.__resources.get_version_info():
            print("[Error]the both of versions between lexpp and dictionary is different. use same version.")
            return False
        else:
            return True

    def lookup(self, surface: str) -> Tuple[Entry]:
        """
        returns a Tuple of entries from given string as lookup key. Duplicating head word is permitted in the dict format. so, the return value should be multiple choice.
        """

        ret = []

        if surface in self.__resources.surface2entry_ids.keys():
            ret = (self.__resources.entries[ix] for ix in self.__resources.surface2entry_ids[surface])

        return ret

    def get_synset(self, entry: Entry) -> Tuple[Entry]:
        """
        returns a Tuple of entries from an entry as lookup key. the tuple has a synset of given entry.
        """

        ret = []
        if entry.group_id in self.__resources.groupid2synonym_ids.keys():
            ret = (self.__resources.entries[ix] for ix in self.__resources.groupid2synonym_ids[entry.group_id])

        return ret

    def get_representative_form(self, entry: Entry) -> str:
        """
        returns a string which is representive form of given entry.
        """
        return self.__resources.groupid_lexid2representive_form[(entry.group_id, entry.lex_id)] if (entry.group_id, entry.lex_id) in self.__resources.groupid_lexid2representive_form.keys() else ""

    def get_common_category_id_set(self, surfaces: List[str]) -> Set[int]:
        """
        Checks whether all of surfaces in the input list belong to same group or not.
        The returned list has group ids which is commonly assigined to input surfaces.
        """

        cat_lst = []

        for surface_i in surfaces:
            cat_lst.append([x.group_id for x in self.lookup(surface_i)])

        if len(cat_lst) == 0:
            return set()

        return set.intersection(*[set(x) for x in cat_lst])