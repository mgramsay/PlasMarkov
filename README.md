<img src="plasmarkov_icon.jpeg" alt="PlasMarkov logo" title="PlasMarkov logo" width="100"/>
# PlasMarkov
A Twitter bot which generates random statements using Markov chains ([@plasmarkov](https://twitter.com/plasmarkov)).

PlasMarkov was intended to generate vaguely scientific sounding statements (of dubious accuracy) based off of the author's PhD thesis (thesis not included), but should work with any body of text.

## Generating Markov chains
Running the `plasmarkov.py` script will use Markov chains to randomly generate a statement no more than 140 characters long. The script will look for and, if found, use an existing transition matrix in generating the statement. If no transition matrix file is found, it will generate one using one of the example text files. You can generate a transition matrix from their own text file by passing the script the name of the file: `python plasmarkov.py my_file.txt`

Once you have run the script passing a text file, the transition matrix is saved, and all further runs without a specified file will use that transition matrix.

The tweet generated is saved to disk ready to be posted to Twitter by the `send_tweet.py` script.

## Using as a Twitter bot
In order to hook use PlasMarkov with a Twitter account, you need to supply it with the keys and access tokens. Create a file named `secrets.py` and populate with the following:
```python
C_KEY = "" # Consumer key
C_SECRET = "" # Consumer secret
A_TOKEN = "" # Access token
A_TOKEN_SECRET = "" # Access token secret
```
For details on how to set up a Twitter app and obtain the necessary keys and tokens see the following guides:  
    [How to create a Twitter bot](http://blog.mollywhite.net/twitter-bots-pt2/)  
    [How To Write a Twitter Bot with Python and tweepy](http://www.dototot.com/how-to-write-a-twitter-bot-with-python-and-tweepy/)

Once a tweet has been created using the `plasmarkov.py` script, it can be posted to Twitter by running the `send_tweet.py` script.
