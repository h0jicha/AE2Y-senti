import sys
import tweepy
import datetime

sys.path.append('../')
from twitter_token_getter import load_twitter_tokens


def get_tweets(query, path_output, count=15):
    list_tweets = []

    dict_token = load_twitter_tokens()

    auth = tweepy.OAuthHandler(
        dict_token['consumer_key'], dict_token['consumer_secret'])
    auth.set_access_token(
        dict_token['access_token'], dict_token['access_secret'])

    api = tweepy.API(auth, wait_on_rate_limit=True)

    # index = 0
    for tweet in api.search_tweets(q=query, lang='ja', count=count, tweet_mode='extended'):

        # つぶやき時間がUTCのため、JSTに変換  ※デバッグ用のコード
        jsttime = tweet.created_at + datetime.timedelta(hours=9)
        print(jsttime)

        list_tweets.append(f'{tweet.id},{tweet.created_at}')
        
        # f'[{index}]<{tweet.id},{tweet.created_at}> {tweet.full_text}\n---------------------------------------\n')
        # index += 1
        # print("\r", index + 1 if index != count else '\ncompleted getting\n', end="")

    fname = r"'" + path_output + "'"
    fname = fname.replace("'", "")

    with open(fname, "w", encoding="utf-8") as f:
        f.writelines(list_tweets)


if __name__ == '__main__':
    QUERY = "新型肺炎 OR コロナ OR ウイルス OR ウィルス OR 武漢 OR デルタ OR オミクロン OR デルタクロン OR 感染者数 - RT"
    PATH_OUTPUT = '../_data/tweets0000.txt'

    get_tweets(QUERY, PATH_OUTPUT)
