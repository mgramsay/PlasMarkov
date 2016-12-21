# -*- coding: utf-8 -*-
# Copyright (c) 2016 Martin Ramsay
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

"""
A simple script to post pre-prepared messages to twitter.
"""

import os

import markovbot
import tweet

def main():
    """
    Main program
    """
    os.chdir(os.path.dirname(os.path.realpath(__file__)))
    markov = markovbot.Bot()
    if os.path.isfile(markovbot.TWEET_FILE):
        read_file = open(markovbot.TWEET_FILE, 'r')
        saved_tweet = read_file.read()
        read_file.close()
        log_msg = tweet.send(saved_tweet)
    else:
        log_msg = 'File "' + markovbot.TWEET_FILE + '" not found'
    tweet.log(log_msg, markov.log)

if __name__ == '__main__':
    main()
