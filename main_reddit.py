import logging
import tweet_with_db
import praw
import time
import datetime
redditlist = []
def main():
        logging.basicConfig(filename='tweet.log', level=logging.INFO)
        st = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')
        logging.info('Tweet log for: '+ st)
        r = praw.Reddit(user_agent='ryan_test_app')
        subreddit = r.get_subreddit("todayilearned")
        for submission in subreddit.get_hot(limit=20):
                if len(submission.title) <=164:
                        sub = submission.title
                        redditlist.append(sub)
        
        redditlist.remove(redditlist[0])
        for r in redditlist:
                if tweet_with_db.tweet_it(r):
                        logging.info('Finished')
                        break


if __name__ == '__main__':
        main()
