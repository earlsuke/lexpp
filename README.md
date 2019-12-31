## lexpp : 同義語辞書による日本語テキストへの前処理ツール

**このモジュールは開発中です**

### このモジュールについて

このモジュールはトークナイズされた辞書登録単位への同義語関連の処理を提供します．
日本語における同義語が収められたデフォルト辞書として[SudachiDict](https://github.com/WorksApplications/SudachiDict)の[synonym辞書](https://github.com/WorksApplications/SudachiDict/blob/develop/docs/synonyms.md)
を利用しています．

### インストール方法

```pip install lexpp```

### 使い方

```python
import lexpp as lp
pp = lp.Lexpp()
```

現在のバージョンでは，下記の機能を提供しています．

1. 文字列を辞書引きして，辞書に登録されている情報(Entry)を呼び出す．  lookup(surface: str) -> Tuple(Entry)
```python
TESTCASE = "マンガ喫茶"
result = pp.lookup(TESTCASE)
```

2. Entryをキーとして，同じグループに登録されている文字列のタプルを得る．  get_synset(e: Entry) -> Tuple(str)
```python
entry = result[0]
synset = pp.get_synset(entry)
# synset = ["漫画喫茶", "まんが喫茶", "マンガ喫茶", "漫喫", "まん喫", "マン喫"]
```

3. Entryをキーとして，代表表記として登録されている文字列を得る．      get_representive_form(e: Entry) -> str
```python
repr_form = pp.get_representive_form(entry)
# repr_form = "漫画喫茶"
```

4. 複数の文字列をクエリとして，共通して登録されているグループIDの集合を得ます．共通して登録されているグループが存在しない場合は，空の集合が返されます． get_common_category_id_set(surfaces: List[str]) -> Set[int]
```python
TESTCASE_LIST = ["漫画喫茶", "まんが喫茶", "マンガ喫茶", "漫喫", "まん喫", "マン喫"]
gid_set = pp.get_common_category_id_set(TESTCASE_LIST)
# gid_set = {27}
```

サンプルコードを下記に示します．

[samples/sample.py](samples/sample.py)

### 独自辞書の作り方

```python -m lexpp.dict_builder {your lexicon} {output filename}```

注意点: 入力ファイルは[synonym辞書](https://github.com/WorksApplications/SudachiDict/blob/develop/docs/synonyms.md)と同じフォーマットであることを想定しています．

ビルド後，Lexppクラスのインスタンスのパラメータとしてファイル名を指定してください．

```python
pp = Lexpp(external_dict_path = {your dictionary})
```

### ライセンス

[Apache 2.0ライセンス](http://www.apache.org/licenses/LICENSE-2.0)の条件下にて，利用していただけます．
このソフトウェアには, [Apache 2.0ライセンス](http://www.apache.org/licenses/LICENSE-2.0)で配布されている製作物が含まれています.

### 参考文献

* 有用なデータセットの公開に感謝します．[SudachiDict](https://github.com/WorksApplications/SudachiDict)

------------------------------------

## lexpp: lexical pre-processing module for Japanese text

***THIS MODULE IS UNDER DEVELOPING***

### What this module is

  This module provides you to pre-process Japanese text by using lexical knowledge. The default dictionary is built based on [Sudachi synonym dict](https://github.com/WorksApplications/SudachiDict/blob/develop/docs/synonyms.md).


### How to install
```pip install lexpp```

### How to use

```python
import lexpp as lp
pp = lp.Lexpp()
```

The current version of the software provides the following utilities.

1. Lookup a key string from the dictionary to get lexical entities.    lookup(surface: str) -> Tuple(Entry)
```python
TESTCASE = "マンガ喫茶"
result = pp.lookup(TESTCASE)
```
2. Lookup a key entry to obtain a synset(a tuple of synonyms).  get_synset(e: Entry) -> Tuple(str)
```python
entry = result[0]
synset = pp.get_synset(entry)
# synonyms = ["漫画喫茶", "まんが喫茶", "マンガ喫茶", "漫喫", "まん喫", "マン喫"]
```
3. Transform a key entry into a string of representive form.  get_representive_form(e: Entry) -> str
```python
repr_form = pp.get_representive_form(entry)
# repr_form = "漫画喫茶"
```
4. Lookup a set of group id which is commonly registered among the input surface list. If no groups existed , an empty set will be returned.  get_common_category_id_set(surfaces: List[str]) -> Set[int]
```python
TESTCASE_LIST = ["漫画喫茶", "まんが喫茶", "マンガ喫茶", "漫喫", "まん喫", "マン喫"]
gid_set = pp.get_common_category_id_set(TESTCASE_LIST)
# gid_set = {27}
```

For more details, See [samples/sample.py](samples/sample.py)

### How to build your dictionary

```python -m lexpp.dict_builder {your lexicon} {output filename}```

NOTE: The input file must be formatted by [the Sudachi synonym dict format]((https://github.com/WorksApplications/SudachiDict/blob/develop/docs/synonyms.md).

When instantiating Lexpp class, specify to your dictionary as a parameter.

```pp = Lexpp(external_dict_path = {your dictionary})```

### License

This software is licensed under [Apache 2.0](http://www.apache.org/licenses/LICENSE-2.0).

This software contains the derivative from the product developed under [Apache 2.0](http://www.apache.org/licenses/LICENSE-2.0).

### References
* Thanks to [SudachiDict](https://github.com/WorksApplications/SudachiDict) for releasing useful resources.
