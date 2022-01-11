import tweepy

import os
from os.path import join, dirname
from dotenv import load_dotenv

#Twitter APIを使用するためのConsumerキー、アクセストークン設定
load_dotenv( verbose = True )
dotenv_path = join( dirname( __file__ ), '.env' )
load_dotenv( dotenv_path )
consumer_key = os.environ.get( "TWITTER_CONSUMER_KEY" )
consumer_secret = os.environ.get( "TWITTER_CONSUMER_SECRET" )
access_token = os.environ.get( "TWITTER_ACCESS_TOKEN" )
access_token_secret = os.environ.get( "TWITTER_ACCESS_SECRET" )

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

# 検索する文章
search_text = 'コロナ ワクチン'

# 検索する
search_results = api.search_tweets(q=search_text, count=100, lang='ja', result_type='mixed')

# 検索結果を1件ずつ出力する
for status in search_results:
    print('---------------------------------------')
    user = status.user
    print('{}(@{}) フォロー数:{}, フォロワー数:{}\n\n{}\n\nいいね:{}, リツイート:{}'
          .format(user.name, user.screen_name, user.friends_count, user.followers_count, status.text,
                  status.favorite_count, status.retweet_count))

#public_tweets = api.home_timeline()
#for tweet in public_tweets:
#    print(tweet.text)
