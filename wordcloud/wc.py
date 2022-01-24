import re
import MeCab
from wordcloud import WordCloud

from googletrans import Translator

import sys
sys.path.append('../')
from twitter_token_getter import load_font_path


def get_word_str(text, NG_words = []):
    mecab = MeCab.Tagger()
    parsed = mecab.parse(text)
    lines = parsed.split('\n')
    lines = lines[0:-2]
    list_word = []

    for line in lines:
        tmp = re.split('\t|,', line)

        # 名詞のみ対象
        if tmp[1] in ["名詞"]:
            # さらに絞り込み
            if tmp[2] in ["一般", "固有名詞"]:
                list_word.append(tmp[0])
                
    list_word = " ".join(list_word)    
    
    for word in NG_words:
        list_word = list_word.replace(word, '')

    return list_word


if __name__ == '__main__':
    NG_WORDS = ['新型肺炎', 'コロナ', 'ウイルス', 'ウィルス', '武漢', 'デルタ株', 'オミクロン株', 'デルタクロン株', '感染者数']
    date = '01232000'
    PATH_TEXTS_READY = f'../_data/tweet_texts_ready_{date}.txt'
    PATH_WC = f'../_data/wordcloud_{date}.png'
    FONT_PATH = load_font_path()

    read_text = open(PATH_TEXTS_READY, encoding="utf8").read()
    word_str = get_word_str(read_text, NG_WORDS)
    
    print(word_str)

    wc = WordCloud(font_path=FONT_PATH, max_font_size=40).generate(word_translated)

    wc.to_file(PATH_WC)
