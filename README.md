# AE2Y-senti（仮）

日本語ツイートを収集して、感情分析します。

tweets収集：tweepy

感情分析器：daigo/bert-base-japanese-sentiment（Huggingface Transformers）

形態素解析：MeCab

可視化：WordCloud

## つかいかた
- 簡単なツイート収集と感情分析：`python script.py`

Twitter APIの利用申請が必要です。

- WordCloud：`python wc.py`

MeCabや日本語Font（私はIPAexGothicを使用）のインストールが必要です。
