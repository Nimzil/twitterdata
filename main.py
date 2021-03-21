import sys
from tweepy import OAuthHandler, API
import os


def twitter_auth():
    """
    Setup Twitter Authentication.
    :return: tweepy.oAuthHandler object
    """
    try:
        API_KEY = os.environ.get('API_KEY')
        API_SECRET = os.environ.get('API_SECRET')
        BEARER_TOKEN = os.environ.get('TOKEN')
        ACCESS_TOKEN = os.environ.get('ACCESS_TOKEN')
        TOKEN_SECRET = os.environ.get('TOKEN_SECRET')
    except KeyError:
        sys.stderr.write('Twitter Env variables not set.')
        sys.exit(1)
    auth = OAuthHandler(API_KEY, API_SECRET)
    auth.set_access_token(ACCESS_TOKEN, TOKEN_SECRET)
    return auth

def twitter_client():
    """
    Setup Twitter API Client
    :return: tweepy.API object
    """
    auth = twitter_auth()
    api = API(auth)

    return api




