#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tweepy
import codecs
import sys
import os
import config
from xml.sax.saxutils import unescape

sys.stdin = codecs.getreader('utf-8')(sys.stdin)
sys.stdout = codecs.getwriter('utf-8')(sys.stdout)

def replace(s):
    s = unicode(s)
    s = unescape(s)
    s = ' '.join(s.split())
    return s

def main():
    if len(sys.argv)<3:
        print "Usage: %s userid path" % sys.argv[0]
        return
    user_id = sys.argv[1]
    since_id = sys.argv[2] + '.since_id'
    tweet = sys.argv[2] + '.tsv'

    auth = tweepy.OAuthHandler(config.consumer_key, config.consumer_secret)
    auth.set_access_token(config.access_key, config.access_secret)
    api = tweepy.API(auth)

    arg = {'id': user_id}
    if os.path.exists(since_id):
        since_id_file = codecs.open(since_id, 'r', 'utf-8')
        arg['since_id'] = since_id_file.readline().rstrip()
        since_id_file.close()
    
    tsv = []
    ids = []
    try:
        user_statuses = tweepy.Cursor(api.user_timeline, **arg).items(3200)
        for user_status in user_statuses:
            item = '\t'.join([replace(user_status.text), str(user_status.created_at), str(user_status.id)])
            tsv.append(item + "\n")
            ids.append(user_status.id)
    except tweepy.error.TweepError, e:
        print >>sys.stderr, "tweepy error occurred: error status " + str(e.reason)
        sys.exit()
    
    if len(tsv)==0:
        return

    tsv.reverse()
    tweet_file = codecs.open(tweet, 'a', 'utf-8')
    tweet_file.writelines(tsv)
    tweet_file.close()

    since_id_file = codecs.open(since_id, 'w', 'utf-8')
    since_id_file.write(str(ids[0]))
    since_id_file.close()
    
if __name__ == "__main__":
  main()
