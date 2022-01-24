import sys
sys.path.append('../')
from twitter_token_getter import load_twitter_tokens
from preprocessor import preprocess

import tweepy
from pytz import timezone

import pandas as pd

class IDStream(tweepy.Stream):    
    PATH_IDS = '../_data/tweet_ids_2000_st.csv'
    MAX_COUNT = 500
    path_output = PATH_IDS
    
    def set_members(self):
        self.i = 0
        self.list_id = []
        self.list_date = []

    def on_status(self, status):
        
        print(f"{self.i}: {status.id}")

        status.created_at = status.created_at.astimezone(timezone('Asia/Tokyo'))

        self.list_id.append(status.id)
        self.list_date.append(status.created_at)
        
        self.i += 1
        # print("\r", self.i+1 if self.i != self.MAX_COUNT else '\ncompleted getting\n', end="")
        
        if self.i == self.MAX_COUNT:
            print(f'\nlist_id length:{len(self.list_id)}')
            fname = r"'" + self.path_output + "'"
            fname = fname.replace("'", "")

            lst = list(zip(self.list_id, self.list_date))
            df = pd.DataFrame(lst, columns=['id', 'created_at'])

            df.to_csv(self.path_output)
            
            self.disconnect()
            
def do_auth():
    dict_token = load_twitter_tokens()

    auth = tweepy.OAuthHandler(
        dict_token['consumer_key'], dict_token['consumer_secret'])
    auth.set_access_token(
        dict_token['access_token'], dict_token['access_secret'])

    api = tweepy.API(auth, wait_on_rate_limit=True)

    return api

def get_tweet_ids(list_keyword, path_output, lang='ja'):
    
    dict_token = load_twitter_tokens()
    
    stream = IDStream(
    dict_token['consumer_key'], dict_token['consumer_secret'],
    dict_token['access_token'], dict_token['access_secret']
    )
    
    stream.set_members()
    
    stream.filter(track=list_keyword, languages=[lang])


def get_tweet_texts(api, path_input, path_output):
    list_text = []

    df = pd.read_csv(path_input)

    for id in df['id'].to_list():
        text = f'[{id}]\n'
        text += api.get_status(id=id).text
        text += '\n---------------------------------------\n'
        list_text.append(text)

    print(f'list_text length:{len(list_text)}')

    fname = r"'" + path_output + "'"
    fname = fname.replace("'", "")

    with open(fname, "w", encoding="utf-8") as f:
        f.writelines(list_text)

if __name__ == '__main__':

    QUERY = "新型肺炎 OR コロナ OR ウイルス OR ウィルス OR 武漢 OR デルタ株 OR オミクロン株 OR デルタクロン株 OR 感染者数 -RT -iHerb"
    LIST_KEYWORD = ["新型肺炎", "コロナ", "ウイルス", "ウィルス", "武漢", "デルタ株", "オミクロン株", "デルタクロン株", "感染者数", "-RT", "-iHerb"]
    PATH_IDS = '../_data/tweet_ids_2000.csv'
    PATH_TEXTS = '../_data/tweet_texts_2000.csv'
    PATH_TEXTS_READY = '../_data/tweet_texts_ready_2000.txt'
    count = 500
    
    api = do_auth()

    list_id = get_tweet_ids(LIST_KEYWORD, PATH_IDS)
    get_tweet_texts(api, PATH_IDS, PATH_TEXTS)
    preprocess(PATH_TEXTS, PATH_TEXTS_READY)