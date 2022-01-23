from io import StringIO
import os
import re

from transformers import pipeline 
from transformers import AutoModelForSequenceClassification 
from transformers import BertJapaneseTokenizer 

PATH_INPUT = '_data/tweets.txt'
PATH_OUTPUT = '_data/output0000.txt'

def analyze():
     
    TARGET_TEXT = "誰でもできる感情分析です。簡単であるので、気軽に試してみましょう。"

    print('prepare analyzing')
     
    model = AutoModelForSequenceClassification.from_pretrained('daigo/bert-base-japanese-sentiment') 
    tokenizer = BertJapaneseTokenizer.from_pretrained('cl-tohoku/bert-base-japanese-whole-word-masking') 
    nlp = pipeline("sentiment-analysis", model=model, tokenizer=tokenizer) 

    print('start analyzing')
     
    #reg = '\[[0-9]+\]'
    reg = '---------------------------------------'
    dict = {}
    buf = ''
    with open(PATH_INPUT) as f:
        for line in f:
            # ツイートを読み切るまでbufに追加
            if re.search(reg,line) is None:
                buf += line
                continue
            senti = nlp(buf)
            dict.setdefault(buf,senti)
            print(buf)
            print(str(senti))
            print("\n")
            buf = ''

    print('write output')

    with open(PATH_OUTPUT, "w") as f:
        for k, v in dict.items():
            f.write(k)
            f.write(str(v))
            f.write('\n---------------------------------------\n')

    print('done')
    
if __name__ == '__main__':
    analyze()