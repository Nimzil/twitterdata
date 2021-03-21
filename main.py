import string, sys, time
from tweepy import Stream
from tweepy.streaming import StreamListener
from tweet_client import twitter_auth


class CustomListener(StreamListener):
    """
    Custom StreamListener for streaming twitter data
    """

    def __init__(self, fname):
        safe_fname = format_filename(fname)
        self.outfile = f'stream_{safe_fname}.jsonl'

    def on_data(self, data):
        try:
            with open(self.outfile, 'a') as f:
                f.write(data)
                return True
        except BaseException as e:
            sys.stderr.write(f"Error on_data: {e} \n")
            time.sleep(5)
        return True

    def on_error(self, status):
        if status == 420:
            sys.stderr.write("Rate Limit Exceeded \n")
            return False
        else:
            sys.stderr.write(f"Error {status} \n")
            return True


def format_filename(fname):
    """
    Convert fname into a safe string for a filename.
    :param fname:
    :return: string
    """
    return ''.join(convert_valid(one_char) for one_char in fname)


def convert_valid(one_char):
    """
    Convert a character into a "_" if "invalid"
    :param one_char:
    :return: string
    """
    valid_chars = f"-_.{string.ascii_letters, string.digits}"
    if one_char in valid_chars:
        return one_char
    else:
        return "_"


if __name__ == '__main__':
    query = sys.argv[1:]  # list of CLI arguments
    query_fname = " ".join(query)
    auth = twitter_auth()
    twitter_stream = Stream(auth, CustomListener(query_fname))
    twitter_stream.filter(track=query, is_async=True)
