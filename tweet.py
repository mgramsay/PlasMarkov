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
Handles the linking to twitter.
"""

import os
from time import gmtime, strftime
import tweepy

from secrets import *

class Tweet(object):
    """
    Collection of methods to handle the twitter interface.
    """
    def __init__(self):
        """
        Initialise the tweet object.
        """
        return

    def send(self, text):
        """
        Post a message to twitter.
        """
        auth = tweepy.OAuthHandler(C_KEY, C_SECRET)
        auth.set_access_token(A_TOKEN, A_TOKEN_SECRET)
        api = tweepy.API(auth)

        try:
            api.update_status(text)
        except tweepy.error.TweepError as err:
            return err.message
        else:
            return 'Tweeted: ' + text

    def log(self, message, logfile_name):
        """
        Update the log file.
        """
        path = os.path.realpath(os.path.join(os.getcwd(),
                                             os.path.dirname(__file__)))
        with open(os.path.join(path, logfile_name), 'a+') as logfile:
            logtime = strftime('%d %b %Y %H:%M:%S', gmtime())
            logfile.write(logtime + ' ' + message + '\n')
        return
