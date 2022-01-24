import os
from os.path import join, dirname
from dotenv import load_dotenv


def load_twitter_tokens():
    token_dict = {}

    dotenv_path = join(dirname(__file__), '.env')
    load_dotenv(verbose=True, dotenv_path=dotenv_path)

    token_dict['consumer_key'] = os.environ.get("TWITTER_CONSUMER_KEY")
    token_dict['consumer_secret'] = os.environ.get("TWITTER_CONSUMER_SECRET")
    token_dict['access_token'] = os.environ.get("TWITTER_ACCESS_TOKEN")
    token_dict['access_secret'] = os.environ.get("TWITTER_ACCESS_SECRET")

    return token_dict


def load_font_path():
    dotenv_path = join(dirname(__file__), '.env')
    load_dotenv(verbose=True, dotenv_path=dotenv_path)

    return os.environ.get("FONT_PATH")
