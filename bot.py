import sys

import markovbot
import tweet

def main(corpus):
    markov = markovbot.bot()
    tweet_text = markov.build_tweet(corpus)

    new_tweet = tweet.tweet()
    log_msg = new_tweet.send(tweet_text)
    new_tweet.log(log_msg, markov.log)

if __name__ == '__main__':
    corpus = None
    if len(sys.argv) > 1:
        corpus = sys.argv[1]
    main(corpus)
