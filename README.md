## lexpp : 同義語辞書による日本語テキストへの前処理ツール

**このモジュールは開発中です**

### このモジュールについて

このモジュールはトークナイズされた辞書登録単位への同義語関連の処理を提供します．
日本語における同義語が収められたデフォルト辞書として[SudachiDict](https://github.com/WorksApplications/SudachiDict)の[synonym辞書](https://github.com/WorksApplications/SudachiDict/blob/develop/docs/synonyms.md)
を利用しています．

### インストール方法

```pip install lexpp```

### 使い方

現在のバージョンでは，下記の機能を提供しています．

1. 文字列を辞書引きして，辞書に登録されている情報(Entry)を呼び出す．  lookup(surface: str) -> Tuple(Entry)
2. Entryをキーとして，同じグループに登録されている文字列集合を得る．  get_synset(e: Entry) -> Tuple(str)
3. Entryをキーとして，代表表記として登録されている文字列を得る．      get_representive_form(e: Entry) -> str

サンプルコードを下記に示します．

[samples/sample.py](samples/sample.py)

### 独自辞書の作り方

```python -m lexpp.dict_builder --input {your dictioanry} --output {output filename}```

注意点: 入力ファイルは[synonym辞書](https://github.com/WorksApplications/SudachiDict/blob/develop/docs/synonyms.md)と同じフォーマットであることを想定しています．

ビルド後，Lexppクラスのインスタンスのパラメータとしてファイル名を指定してください．

```pp = Lexpp(external_dict_path = {your dictionary})```

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

The current version of the software provides the following utilities.

1. Lookup a key string from the dictionary to get lexical entities.    lookup(surface: str) -> Tuple(Entry)
2. Lookup a key entry to obtain a synset(a set of synonyms).  get_synset(e: Entry) -> Tuple(str)
3. Transform a key entry into a string of representive form.  get_representive_form(e: Entry) -> str

For more details, See [samples/sample.py](samples/sample.py)

### How to build your dictionary

```python -m lexpp.dict_builder --input {your dictioanry} --output {output filename}```

NOTE: The input file must be formatted by [the Sudachi synonym dict format]((https://github.com/WorksApplications/SudachiDict/blob/develop/docs/synonyms.md).

When instantiating Lexpp class, specify to your dictionary as a parameter.

```pp = Lexpp(external_dict_path = {your dictionary})```

### License

This software is licensed under [Apache 2.0](http://www.apache.org/licenses/LICENSE-2.0).

This software contains the derivative from the product developed under [Apache 2.0](http://www.apache.org/licenses/LICENSE-2.0).

### References
* Thanks to [SudachiDict](https://github.com/WorksApplications/SudachiDict) for releasing useful resources.
