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

def main():
    parser = OptionParser()
    parser.add_option("-i", "--in_reply_to_status_id", dest="reply",
                      help="in_reply_to_status_id")
    parser.add_option("--lat", dest="lat",
                      help="latitude")
    parser.add_option("--long", dest="long",
                      help="longitude")
    (options, args) = parser.parse_args()

    auth = tweepy.OAuthHandler(config.consumer_key, config.consumer_secret)
    auth.set_access_token(config.access_key, config.access_secret)
    api = tweepy.API(auth)
    
    arg = {}
    arg["status"] = " ".join(args)

    if options.lat:
        arg["lat"] = options.lat
    if options.long:
        arg["long"] = options.long

    print util.toString(api.update_status(**arg))

if __name__ == "__main__":
  main()

