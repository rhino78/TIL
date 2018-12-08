#!/usr/bin/env python
import logging
import tweet_with_db
import praw
import time
import datetime


redditlist = []


def main():
    logging.basicConfig(filename='/home/ryan/github/TIL/tweet.log', level=logging.INFO)
    st = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')
    logging.info('Tweet log for: '+ st)
    r = praw.Reddit(client_id='JgiAaoEUbf86tA',
        client_secret='bz4rt2sUhhQs0suOR_2uq4QuIhA',
        password='thomas08',
        user_agent='tweet_bot',
        username='rhino_78')

    subreddit = r.subreddit("todayilearned")
    for submission in subreddit.hot(limit=20):
        if len(submission.title) <= 140:
            sub = submission.title
            redditlist.append(sub)

    redditlist.remove(redditlist[0])
    for r in redditlist:
        if tweet_with_db.tweet_it(r):
            logging.info('Finished')
            break


if __name__ == '__main__':
    main()
