import sys
from twitter_token_getter import load_font_path
sys.path.append('./extractor')
from extractor import tweet_extractor, preprocessor
sys.path.append('./analyzer')
from analyzer import analyzer_with_mlask, analyzer_with_bert
sys.path.append('./visualizer')
from visualizer import wc

import datetime

if __name__ == '__main__':
    print(f'now: {datetime.datetime.today()}')

    # 検索文字列
    QUERY = "新型肺炎 OR コロナ OR ウイルス OR ウィルス OR 武漢 OR デルタ株 OR オミクロン株 -RT -iHerb"
    NG_WORDS_WC = ['新型肺炎', 'コロナ', 'ウイルス', 'ウィルス', '武漢', 'デルタ株', 'オミクロン株']
    
    # 検索日時
    day = 22 # この日の
    hour = 18 # この１時間について、10分刻みにデータを取得する
    minute = 0 
    list_until = [f'2022-01-{day}_{hour+1}:00:00_JST']
    for minute in range(0,51,10):
        list_until.append(f'2022-01-{day}_{hour}:{minute}:00_JST')
    
    date = f'01{day}{hour}00'
    
    PATH_IDS = f'_data/ids_{date}.csv'
    PATH_TEXTS = f'_data/texts_{date}.txt'
    PATH_TEXTS_READY = f'_data/texts_ready_{date}.txt'
    PATH_SENTIMENT_VALUES_MLASK = f'_data/df_mlask_{hour}00.csv'
    PATH_SENTIMENT_VALUES_BERT = f'_data/values_bert_{date}.txt'
    PATH_WC = f'_data/wc_{date}.png'
    FONT_PATH = load_font_path()

    # get tweets and preprocess    
    api = tweet_extractor.do_auth()
    
    print('getting tweet ids...')
    for until in list_until:
        tweet_extractor.get_tweet_ids(api, QUERY, PATH_IDS, count=100, until=until)
    print('getting tweet ids done')

    print('getting tweet texts...')
    tweet_extractor.get_tweet_texts(api, PATH_IDS, PATH_TEXTS)
    print('getting tweet texts done')
    
    print('preprocessing...')
    preprocessor.preprocess(PATH_TEXTS, PATH_TEXTS_READY)
    print('preprocessing done')
    
    
    # sentiment analysis
    print('analyzing tweets with ML-Ask...')
    analyzer_with_mlask.analyze(PATH_TEXTS_READY, PATH_SENTIMENT_VALUES_MLASK, day)
    print('analyzing tweets with ML-Ask done')
    
    """
    print('analyzing tweets with BERT...')
    analyzer_with_bert.analyze(PATH_TEXTS_READY, PATH_SENTIMENT_VALUES_BERT)
    print('analyzing tweets with BERT done')
    """
    
    print('analyzing tweets done')
    
    
    # wordcloud
    print('visualizing tweets...')
    
    wc.visualize(FONT_PATH, PATH_TEXTS_READY, PATH_WC, NG_WORDS_WC)
    
    print('visualizing tweets done')
    
    
    print('script done')
    
    
