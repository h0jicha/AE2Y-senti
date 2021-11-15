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

public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(tweet.text)
