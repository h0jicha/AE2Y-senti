from io import StringIO
import os
import re

from transformers import pipeline
from transformers import AutoModelForSequenceClassification
from transformers import BertJapaneseTokenizer

def analyze(path_input, path_output):

    print('prepare to analyze')

    model = AutoModelForSequenceClassification.from_pretrained(
        'daigo/bert-base-japanese-sentiment')
    tokenizer = BertJapaneseTokenizer.from_pretrained(
        'cl-tohoku/bert-base-japanese-whole-word-masking')
    nlp = pipeline("sentiment-analysis", model=model, tokenizer=tokenizer)

    print('start analyzing')

    #reg = '\[[0-9]+\]'
    reg = '---------------------------------------'
    dict = {}
    buf = ''
    with open(path_input) as f:
        for line in f:
            # ツイートを読み切るまでbufに追加
            if re.search(reg, line) is None:
                buf += line
                continue
            value = nlp(buf)
            dict.setdefault(buf, value)
            print(buf)
            print(str(value))
            print("\n")
            buf = ''

    print('write output')

    with open(path_output, "w") as f:
        for k, v in dict.items():
            f.write(k)
            f.write(str(v))
            f.write('\n---------------------------------------\n')

    print('done')


if __name__ == '__main__':
    PATH_TEXTS_READY = '../_data/tweet_texts_ready_0000.csv'
    PATH_SENTIMENT_VALUES = '../_data/values_0000.csv'
    
    analyze(PATH_TEXTS_READY, PATH_SENTIMENT_VALUES)
