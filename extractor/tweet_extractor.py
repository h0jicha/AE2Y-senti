import sys
sys.path.append('../')
from twitter_token_getter import load_twitter_tokens
from preprocessor import preprocess

import tweepy
from pytz import timezone

import pandas as pd


def do_auth():
    dict_token = load_twitter_tokens()

    auth = tweepy.OAuthHandler(
        dict_token['consumer_key'], dict_token['consumer_secret'])
    auth.set_access_token(
        dict_token['access_token'], dict_token['access_secret'])

    api = tweepy.API(auth, wait_on_rate_limit=True)

    return api


def get_tweet_ids(api, query, path_output, until, lang='ja', count=15):
    list_id = []
    list_date = []

    # get tweet ids
#    i = 0
    for tweet in api.search_tweets(q=query, lang=lang, count=count, tweet_mode='extended', until=until):

        if lang == 'ja':
            tweet.created_at = tweet.created_at.astimezone(
                timezone('Asia/Tokyo'))

        list_id.append(tweet.id)
        list_date.append(tweet.created_at)
        
#        i += 1
#        print("\r", i+1 if i != count else '\ncompleted getting\n', end="")

    print(f'\nlist_id length:{len(list_id)}')

    fname = r"'" + path_output + "'"
    fname = fname.replace("'", "")

    lst = list(zip(list_id, list_date))
    df = pd.DataFrame(lst, columns=['id', 'created_at'])

    df.to_csv(path_output, mode='a')


def get_tweet_texts(api, path_input, path_output):
    list_text = []

    df = pd.read_csv(path_input)

    for id in df['id'].to_list():
        text = f'[{id}]\n'
        try:
            text += api.get_status(id=id).text
        except tweepy.errors.NotFound:
            print(f'tweet id:{id} not found.')
            continue
        text += '\n---------------------------------------\n'
        list_text.append(text)

    print(f'list_text length:{len(list_text)}')

    fname = r"'" + path_output + "'"
    fname = fname.replace("'", "")

    with open(fname, "w", encoding="utf-8") as f:
        f.writelines(list_text)


if __name__ == '__main__':

    QUERY = "新型肺炎 OR コロナ OR ウイルス OR ウィルス OR 武漢 OR デルタ株 OR オミクロン株 OR デルタクロン株 OR 感染者数 -RT -iHerb"
    date = '01232000'
    PATH_IDS = f'../_data/tweet_ids_{date}.csv'
    PATH_TEXTS = f'../_data/tweet_texts_{date}.txt'
    PATH_TEXTS_READY = f'../_data/tweet_texts_ready_{date}.txt'
    count = 100
    
    min = 0
    list_until = [f'2022-01-23_21:00:00_JST',
        f'2022-01-23_20:{min+50}:00_JST',
        f'2022-01-23_20:{min+40}:00_JST',
        f'2022-01-23_20:{min+30}:00_JST',
        f'2022-01-23_20:{min+20}:00_JST',
        f'2022-01-23_20:{min+10}:00_JST']

    api = do_auth()
    
#    for until in list_until:
#        get_tweet_ids(api, QUERY, PATH_IDS, count=count, until=until)

    get_tweet_texts(api, PATH_IDS, PATH_TEXTS)
    
    preprocess(PATH_TEXTS, PATH_TEXTS_READY)
