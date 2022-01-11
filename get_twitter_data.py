import tweepy
import datetime

import os
from os.path import join, dirname
from dotenv import load_dotenv

def gettwitterdata(keyword,dfile):

    # dotenvでapiキー情報を取得する準備
    load_dotenv( verbose = True )
    dotenv_path = join( dirname( __file__ ), '.env' )
    load_dotenv( dotenv_path )

    #Twitter APIを使用するためのConsumerキー、アクセストークン設定
    Consumer_key = os.environ.get( "TWITTER_CONSUMER_KEY" ) 
    Consumer_secret = os.environ.get( "TWITTER_CONSUMER_SECRET" ) 
    Access_token = os.environ.get( "TWITTER_ACCESS_TOKEN" ) 
    Access_secret = os.environ.get( "TWITTER_ACCESS_SECRET" ) 

    #認証
    auth = tweepy.OAuthHandler(Consumer_key, Consumer_secret)
    auth.set_access_token(Access_token, Access_secret)

    api = tweepy.API(auth, wait_on_rate_limit = True)

    #検索キーワード設定 
    q = keyword

    #つぶやきを格納するリスト
    tweets_data =[]

    i = 0
    #カーソルを使用してデータ取得
    for tweet in api.search_tweets(q=q, lang='ja',count=100,tweet_mode='extended'):

        #つぶやき時間がUTCのため、JSTに変換  ※デバッグ用のコード
        #jsttime = tweet.created_at + datetime.timedelta(hours=9)
        #print(jsttime)

        #つぶやきテキスト(FULL)を取得
        tweets_data.append(f'[{i}] {tweet.full_text}\n')
        i = i + 1


    #出力ファイル名
    fname = r"'"+ dfile + "'"
    fname = fname.replace("'","")

    #ファイル出力
    with open(fname, "w",encoding="utf-8") as f:
        f.writelines(tweets_data)


if __name__ == '__main__':

    #検索キーワードを入力  ※リツイートを除外する場合 「キーワード -RT 」と入力
    print ('====== Enter Search KeyWord   =====')
    keyword = input('>  ')

    #出力ファイル名を入力(相対パス or 絶対パス)
    print ('====== Enter Tweet Data file =====')
    dfile = input('>  ')

    gettwitterdata(keyword,dfile)
