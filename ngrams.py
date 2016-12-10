'''
Module to handle sentence fragments (ngrams, punctuation, etc)
'''


PUNCTUATION = (',', '.', '?', '!', ':', ';')
TERMINATOR = ('.', '?', '!')

def build_ngram(first_word, second_word):
    if second_word in PUNCTUATION:
        ngram = first_word + second_word
    else:
        ngram = first_word + ' ' + second_word
    return ngram

def split_ngram(ngram):
    if ngram[len(ngram)-1] in PUNCTUATION:
        first_word = ngram[0:len(ngram)-1]
        second_word = ngram[len(ngram)-1]
    else:
        first_word, second_word = ngram.split()
    return first_word, second_word

