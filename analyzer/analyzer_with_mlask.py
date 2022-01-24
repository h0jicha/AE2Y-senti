from io import StringIO
import os
import re

from mlask import MLAsk

def analyze(path_input, path_output):

    print('prepare to analyze')

    emotion_analyzer = MLAsk()
#data = emotion_analyzer.analyze('いや〜なかなかコロナがおさまらなくて大変だなあ。だけどもう少しの辛抱だと思うんだ。大変だと思うけど頑張ろうね。')

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
            value = emotion_analyzer.analyze(buf)
            dict.setdefault(buf, value)
            print(buf)
            print(str(value))
            print("\n")
            buf = ''

    print('write output')

    with open(path_output, "w") as f:
        for k, v in dict.items():
            f.write(str(v)+'\n')

    print('done')


if __name__ == '__main__':
    PATH_TEXTS_READY = '../_data/tweet_texts_ready_0000.csv'
    PATH_SENTIMENT_VALUES = '../_data/values_0000.csv'
    
    analyze(PATH_TEXTS_READY, PATH_SENTIMENT_VALUES)
