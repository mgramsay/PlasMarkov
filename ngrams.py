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
Module to handle sentence fragments (ngrams, punctuation, etc).
"""

from text_handler import PUNCTUATION

GRAM_LENGTH = 2

class Ngram(object):
    """
    Class to manipulate n-grams.
    """
    def __init__(self, word_list):
        """
        Create an n-gram from a given list of words.
        """
        self.ngram = ''
        for iword in xrange(len(word_list)):
            if word_list[iword] in PUNCTUATION or iword == 0:
                self.ngram += word_list[iword]
            else:
                self.ngram += (' ' + word_list[iword])

    def split(self):
        """
        Split the n-gram into its constituent words/punctuation.
        """
        split_ngram = self.ngram.split()
        word_list = []
        for word in split_ngram:
            if word.endswith(PUNCTUATION):
                word_list.append(word[0:len(word)-1])
                word_list.append(word[len(word)-1])
            else:
                word_list.append(word)
        return word_list
