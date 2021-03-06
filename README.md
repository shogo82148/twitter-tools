Twitter Development Tools
=========================

# What's this?
This is command line tools for accessing to the Twitter.

# Install
It requires [tweepy](https://github.com/tweepy/tweepy).
You can use easy_install or pip to install tweepy to you computer.

    $ easy_install tweepy

or

    $ pip install tweepy

Then, clone this repository or decompress .zip/.tar.gz.

# Usage

## crawler.py
Crawling user's tweets tool.

    $ python crawler.py users-id path-to-save

Save user's tweets to "path-to-save.tsv", and recent status id to "path-to-save.since_id".

## update_status.py
Update status using status/update API

    $ python update_state.py --lat=latitude --long=longitude -i in_reply_to_status_id  'tweet'

## stream.py
Get tweets with streaming API

    $ python stream.py # connect to userstream
    $ python stream.py --raw # Show raw JSON data
    $ python stream.py userstream
    $ python stream.py sample
    $ python stream.py retweet
    $ python stream.py firehose
    $ python stream.py filter keywords
