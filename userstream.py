#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tweepy
import config
import codecs
import sys
import util
from optparse import OptionParser

sys.stdin = codecs.getreader('utf-8')(sys.stdin)
sys.stdout = codecs.getwriter('utf-8')(sys.stdout)

class MyListener(tweepy.StreamListener):
    def on_status(self, status):
        print '@%s:%s%s' % (
            status.author.screen_name,
            ' ' * (15-len(status.author.screen_name)),
            status.text,
            )
        sys.stdin.flush()

    def on_delete(self, status_id, user_id):
        print '[delete] %d deleted %d' % (
            user_id,
            status_id,
            )
        sys.stdin.flush()

    def on_limit(self, track):
        print '[limit] %s' % track

    def on_error(self, status_code):
        print '[error] %d' % status_code
        sys.stdin.flush()

    def on_timeout(self):
        print '[timeout]'
        sys.stdin.flush()

class RawListener(tweepy.StreamListener):
    def on_data(self, data):
        print data
        sys.stdin.flush()

def main():
    parser = OptionParser()
    parser.add_option("-r", "--raw", dest="raw",
                      action="store_true", default=False,
                      help="Print raw data")
    parser.add_option("-n", "--nosecure", dest="secure",
                      action="store_false", default=True,
                      help="Do not use https")
    (options, args) = parser.parse_args()

    auth = tweepy.OAuthHandler(config.consumer_key, config.consumer_secret)
    auth.set_access_token(config.access_key, config.access_secret)
    if options.raw:
        listener = RawListener()
    else:
        listener = MyListener()
    stream = tweepy.Stream(auth, listener, secure = options.secure)
    stream.userstream()

if __name__ == "__main__":
  main()

