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
Handles the linking to twitter.
"""

import codecs
import os
from time import gmtime, strftime
import tweepy

from secrets import C_KEY, C_SECRET, A_TOKEN, A_TOKEN_SECRET

def send(text):
    """
    Post a message to twitter.
    """
    auth = tweepy.OAuthHandler(C_KEY, C_SECRET)
    auth.set_access_token(A_TOKEN, A_TOKEN_SECRET)
    api = tweepy.API(auth)

    print ('Sending: ' + text).encode('utf-8')
    try:
        api.update_status(text)
    except tweepy.error.TweepError as err:
        return err.message
    else:
        return 'Tweeted: ' + text

def log(message, logfile_name):
    """
    Update the log file.
    """
    path = os.path.realpath(os.path.join(os.getcwd(),
                                         os.path.dirname(__file__)))
    with codecs.open(os.path.join(path, logfile_name), mode='a+',
                     encoding='utf-8') as logfile:
        logtime = strftime('%d %b %Y %H:%M:%S', gmtime())
        logfile.write(logtime + ' ' + message + '\n')
