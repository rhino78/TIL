#!/usr/bin/env python
import logging
import tweet_with_db
import praw
import time
import datetime
import tweet_creds


redditlist = []


def main():
    logging.basicConfig(filename='/home/ryan/github/TIL/tweet.log', level=logging.INFO)
    st = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')
    logging.info('Tweet log for: ' + st)
    r = praw.Reddit(client_id=tweet_creds.CLIENT_ID,
                    client_secret=tweet_creds.CLIENT_SECRET,
                    password=tweet_creds.PASSWORD,
                    user_agent=tweet_creds.USER_AGENT,
                    username=tweet_creds.USERNAME)

    subreddit = r.subreddit("todayilearned")
    for submission in subreddit.hot(limit=20):
        if len(submission.title) <= 280:
            sub = submission.title
            redditlist.append(sub)

    # if for some reason we didn't get anything, let's not do any work
    if len(redditlist) > 0:
        redditlist.remove(redditlist[0])
        for r in redditlist:
            if tweet_with_db.tweet_it(r):
                logging.info('Finished')
                break


if __name__ == '__main__':
    main()
