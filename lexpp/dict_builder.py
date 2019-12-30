# coding:utf-8

from codecs import open
from sys import stderr
from lexpp.entry import Entry
from lexpp.dictionary import LexicalDictionary

import pickle as pkl
import argparse

LINESEP_LIST = ['\r\n', '\n']
SEPARATOR = ','
VALID_ITEM_SIZE = 11
ID_GROUP_ID = 0
ID_TAIGEN_OR_YOUGEN_FLG = 1
ID_HEAD = 8
UNDEF = "undefined"


class DictBuilder:

    __version_info__ = (1, 1, 0)

    @staticmethod
    def is_representive(entry: Entry):
        return entry.variant_info == 0 and entry.form_type == 0 and entry.abbr_info == 0 and entry.expand_controll_flg == 0

    @staticmethod
    def build(input_filename: str) -> LexicalDictionary:

        dictionary = LexicalDictionary(DictBuilder.__version_info__)

        # parse lines
        with open(input_filename, mode="r", encoding="utf-8") as rb:

            eid = 0
            for line in rb:

                if line == '\n' or line == '\r\n':
                    continue

                # parse
                items = line.split(',')

                # size validation
                if len(items) != VALID_ITEM_SIZE:
                    print("[Warn][format]the size of items is not valid : {}".format(len(items)), file=stderr)
                    print("[Warn][format] {}".format(line), file=stderr)

                # store values
                hw = items[ID_HEAD]

                gid = int(items[ID_GROUP_ID])
                taiyou_flg = int(items[1]) if items[1] != "" else 0
                tenkai_flg = int(items[2]) if items[2] != "" else 0
                # TODO: default?
                goi_num_list = [int(x) for x in items[3].split('/')] if items[3] != "" else [UNDEF]
                gokei_type = int(items[4]) if items[4] != "" else UNDEF
                tenkai_flg = int(items[5]) if items[5] != "" else UNDEF
                tenkai_flg = int(items[5]) if items[5] != "" else UNDEF
                hyouki_yure_flg = int(items[6]) if items[6] != "" else UNDEF

                # TODO: ID
                category = items[7] if items[7] != "" else UNDEF

                e = Entry(surface=hw, group_id=gid)
                e.category = category
                e.variant_info = hyouki_yure_flg
                e.expand_controll_flg = tenkai_flg
                e.declinable_flg = taiyou_flg
                e.form_type = gokei_type

                for lex_i in goi_num_list:
                    e.lex_id = lex_i

                    # check whether is representive
                    if (DictBuilder.is_representive(e)):
                        dictionary.groupid_lexid2representive_form[(e.group_id, e.lex_id)] = hw

                    dictionary.entries.append(e)
                    dictionary.surface2entry_ids[hw].append(eid)
                    dictionary.groupid2synonym_ids[gid].append(eid)

                    eid += 1

        return dictionary


    @staticmethod
    def build_and_export(input_filename: str, output_filename: str):
        dictionary = DictBuilder.build(input_filename)
        with open(output_filename, mode="wb") as product:
            pkl.dump(dictionary, product, protocol=2)


def main():

    ps = argparse.ArgumentParser(description='lexpp dictionary builder')
    # ps.add_argument('-i', '--input', help='input file name')
    ps.add_argument('input', help='input file name')
    ps.add_argument('output', help='output file name')
    args = ps.parse_args()

    input_filename = args.input
    output_filename = args.output

    DictBuilder.build_and_export(input_filename, output_filename)
    print("success")
    print("output file :", output_filename)

if __name__ == "__main__":
    main()
