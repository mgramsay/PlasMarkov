import sys

import markovbot
import tweet

def main(corpus):
    # Check for matrix files
    # Check if corpus file provided
    # Build/load matrices
    # Build tweet
    # Send tweet
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
