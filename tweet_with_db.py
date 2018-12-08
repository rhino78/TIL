import logging
import tweepy
import sqlite3
import tweet_creds
def tweet_it(status):
    auth = tweepy.OAuthHandler(tweet_creds.CONSUMER_KEY, tweet_creds.CONSUMER_SECRET)
    auth.set_access_token(tweet_creds.ACCESS_KEY, tweet_creds.ACCESS_SECRET)
    api = tweepy.API(auth)
    logging.basicConfig(filename='tweet.log', level=logging.INFO)
    logging.info(status)
    try:
        if not_in_db(status):
            api.update_status(status=status)
            log_it(status)
            return True
        else:
            return False
    except tweepy.TweepError as e:
        logging.info(e)
        logging.info(type(e))
        logging.info(e.reason)
        return False
    finally:
        logging.info('Tweeting: ' + status)

def not_in_db(status):
    conn = sqlite3.connect(r"/home/ryan/github/TIL/til.db")
    cursor = conn.cursor()
    cursor.execute('select 1 from tweets where tweet = ?', (status,))
    if cursor.fetchone():
        return False
    else:
        return True

def log_it(status):
    conn = sqlite3.connect(r"/home/ryan/github/TIL/til.db")
    cursor = conn.cursor()
    cursor.execute('insert into tweets(tweet, dateoftweet) values(?, CURRENT_TIMESTAMP)', (status,))
    conn.commit()
    conn.close()

