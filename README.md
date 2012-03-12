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
