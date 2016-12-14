<img src="plasmarkov_icon.jpeg" alt="PlasMarkov logo" title="PlasMarkov logo" style="width: 100px;"/>
# PlasMarkov
A twitter bot which generates random statements using Markov chains ([@plasmarkov](https://twitter.com/plasmarkov)).

PlasMarkov was intended to generate vaguely scientific sounding statements (of dubious accuracy) based off of the author's PhD thesis (thesis not included), but should work with any body of text.

## Using as a twitter bot
In order to hook the bot up to a twitter account, you need to supply it with the keys and access tokens. Create a file named `secrets.py` and populate with the following:
```python
C_KEY = "" # Consumer key
C_SECRET = "" # Consumer secret
A_TOKEN = "" # Access token
A_TOKEN_SECRET = "" # Access token secret
```
For details on how to set up a twitter app and obtain the necessary keys and tokens see the following guides:  
[How to create a Twitter bot](http://blog.mollywhite.net/twitter-bots-pt2/)  
[How To Write a Twitter Bot with Python and tweepy](http://www.dototot.com/how-to-write-a-twitter-bot-with-python-and-tweepy/)

Note that the development branch (`develop`) for PlasMarkov is configured to only send statements to stdout, in order to avoid flooding any twitter feeds with test runs.

