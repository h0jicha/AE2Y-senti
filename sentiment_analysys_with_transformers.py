from io import StringIO
import os
import re
from transformers import pipeline 
from transformers import AutoModelForSequenceClassification 
from transformers import BertJapaneseTokenizer 

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
    with open('./test.txt') as f:
        for line in f:
            # ツイートを読み切るまでbufに追加
            if re.search(reg,line) is None:
                buf += line
                continue
            senti = nlp(buf)
            dict.setdefault(buf,senti)
            print(buf)
            print(senti)
            print("\n")
            buf = ''

    print('write output')

    with open('./output.txt', "w") as f:
        for str, senti in dict.items():
            f.write(str)
            f.write(senti)
            print("\n")