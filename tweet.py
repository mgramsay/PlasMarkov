import os
import tweepy
from time import gmtime, strftime

from secrets import *

class tweet():
    def __init__(self):
        return

    def send(self, text):
#        auth = tweepy.OAuthHandler(C_KEY, C_SECRET)
#        auth.set_access_token(A_TOKEN, A_TOKEN_SECRET)
#        api = tweepy.API(auth)
        
        try:
#            api.update_status(text)
            print text
        except tweepy.error.TweepError as err:
            return err.message
        else:
            return 'Tweeted: ' + text

    def log(self, message, logfile_name):
        path = os.path.realpath(os.path.join(os.getcwd(),
                                             os.path.dirname(__file__)))
        with open(os.path.join(path, logfile_name), 'a+') as logfile:
            logtime = strftime('%d %b %Y %H:%M:%S', gmtime())
            logfile.write(logtime + ' ' + message + '\n')
        return
