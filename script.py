from get_twitter_data import gettwitterdata
from sentiment_analysys_with_transformers import analyze

if __name__ == '__main__':

    #検索キーワードを入力  ※リツイートを除外する場合 「キーワード -RT 」と入力
    print ('====== Enter Search KeyWord   =====')
    keyword = input('>  ') + ' -RT -iHerb'
    print(f'your input:{keyword}')

    #出力ファイル名を入力(相対パス or 絶対パス)
    #print ('====== Enter Tweet Data file =====')
    dfile = 'tweets.txt'

    gettwitterdata(keyword,dfile)

    analyze()
