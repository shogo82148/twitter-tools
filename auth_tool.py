#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import with_statement

import tweepy
import codecs
import sys
import util
import os
import stat

def main():
    consumer_key = raw_input('Your Consumer Key: ').strip()
    consumer_secret = raw_input('Your Consumer Secret: ').strip()
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    
    print 'Please access this URL: ' + auth.get_authorization_url()
    print
    pin = raw_input('Please input verification PIN from twitter.com: ').strip()

    token = auth.get_access_token(verifier=pin)
    print 'Access token:'
    print '  Key: %s' % token.key
    print '  Secret: %s' % token.secret

    with open('config.py.example', 'r') as f:
        config = f.read()

    config = config.replace('Your Consumer Key', consumer_key)
    config = config.replace('Your Consumer Secret', consumer_secret)
    config = config.replace('Your Access Key', token.key)
    config = config.replace('Your Access Secret', token.secret)

    with open('config.py', 'w') as f:
        f.write(config)
    os.chmod('config.py', stat.S_IRUSR | stat.S_IWUSR)

if __name__ == "__main__":
  main()

