#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tweepy

def toString(item, nest=0):
    if isinstance(item, (int, float)):
        return str(item)
    elif isinstance(item, (str, unicode)):
        return item
    elif isinstance(item, tweepy.models.Model):
        result = '\n'
        for name in dir(item):
            val = getattr(item, name)
            if name[0]=='_' or callable(val):
                continue
            if isinstance(item, tweepy.models.Status) and name=='user':
                continue
            result += '%s%s: %s\n' % ('\t'*nest, name, toString(val, nest+1))
        return result
    else:
        return str(item)
