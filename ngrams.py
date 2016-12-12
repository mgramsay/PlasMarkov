'''
Module to handle sentence fragments (ngrams, punctuation, etc)
'''

from text_handler import PUNCTUATION

class ngram():
    def __init__(self, word_list):
        self.ngram = ''
        for iword in xrange(len(word_list)):
            if word_list[iword] in PUNCTUATION or iword == 0:
                self.ngram += word_list[iword]
            else:
                self.ngram += (' ' + word_list[iword])

    def split(self):
        split_ngram = self.ngram.split()
        word_list = []
        for word in split_ngram:
            if word.endswith(PUNCTUATION):
                word_list.append(word[0:len(word)-1])
                word_list.append(word[len(word)-1])
            else:
                word_list.append(word)
        return word_list
