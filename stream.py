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
        sys.stdout.flush()

    def on_delete(self, status_id, user_id):
        print '[delete] %d deleted %d' % (
            user_id,
            status_id,
            )
        sys.stdout.flush()

    def on_limit(self, track):
        print '[limit] %s' % track

    def on_error(self, status_code):
        print '[error] %d' % status_code
        sys.stdout.flush()

    def on_timeout(self):
        print '[timeout]'
        sys.stdout.flush()

class RawListener(tweepy.StreamListener):
    def on_data(self, data):
        print data
        sys.stdout.flush()

def main():
    parser = OptionParser()
    parser.add_option("-r", "--raw", dest="raw",
                      action="store_true", default=False,
                      help="Print raw data")
    parser.add_option("-n", "--nosecure", dest="secure",
                      action="store_false", default=True,
                      help="Do not use https")
    parser.add_option("-f", "--follow", dest="follow",
                      action="store")
    parser.add_option("-l", "--locations", dest="locations",
                      action="store")
    (options, args) = parser.parse_args()

    auth = tweepy.OAuthHandler(config.consumer_key, config.consumer_secret)
    auth.set_access_token(config.access_key, config.access_secret)
    if options.raw:
        listener = RawListener()
    else:
        listener = MyListener()
    stream = tweepy.Stream(auth, listener, secure = options.secure)

    if len(args)==0:
        stream.userstream()
    elif args[0] == 'userstream':
        stream.userstream()
    elif args[0] == 'sample':
        stream.sample()
    elif args[0] == 'retweet':
        stream.retweet()
    elif args[0] == 'firehose':
        stream.firehose()
    elif args[0] == 'filter':
        track = None
        follow = None
        locations = None
        if len(args)>1:
            track = args[1:]
        if options.follow:
            follow = options.follow.split(',')
        if options.locations:
            locations = [float(s) for s in options.locations.split(',')]
        stream.filter(track=track, follow=follow, locations=locations)

if __name__ == "__main__":
  main()

