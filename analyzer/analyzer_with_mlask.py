from io import StringIO
import os
import re

from mlask import MLAsk

import pandas as pd

def analyze(path_input, path_output, index):
    dict_emotion = {
        'suki': 0,
        'ikari': 0,
        'kowa': 0,
        'yasu': 0,
        'iya': 0,
        'aware': 0,
        'takaburi': 0,
        'odoroki': 0,
        'haji': 0,
        'yorokobi': 0,
    }

    print('prepare to analyze')

    emotion_analyzer = MLAsk()
#data = emotion_analyzer.analyze('いや〜なかなかコロナがおさまらなくて大変だなあ。だけどもう少しの辛抱だと思うんだ。大変だと思うけど頑張ろうね。')

    print('start analyzing')

    regLine = '---------------------------------------'
    regId = '\[[0-9]+\]'
    dict = {}
    buf = ''
    with open(path_input) as f:
        for line in f:
            # ツイートを読み切るまでbufに追加
            if re.search(regLine, line) is None:
                buf += line
                continue
            buf = re.sub(regId, '', buf)
            value = emotion_analyzer.analyze(buf)
            dict.setdefault(buf, value['emotion'])
            if value['emotion'] != None:
                l = list(value['emotion'].keys())
                if l[0] == 'text':
                    del l[0]
                for emo in l:
                    dict_emotion[emo] += 1
            buf = ''

#    with open(path_output, "w") as f:
#        for k, v in dict.items():
#            f.write(str(v)+'\n')

#    print(dict_emotion)
    
    # as dataframe
    df = pd.DataFrame([dict_emotion], index = [index])
    df.to_csv(path_output, mode='a')
    
    print(df)

if __name__ == '__main__':
    date = '01232000'
    PATH_TEXTS_READY = f'../_data/tweet_texts_ready_{date}.txt'
    PATH_SENTIMENT_VALUES = f'../_data/values_mlask_{date}.txt'
    
    analyze(PATH_TEXTS_READY, PATH_SENTIMENT_VALUES, 0)
