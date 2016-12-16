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
Generate twitter messages using Markov chains.
"""

import arb_random
import matrices
from ngrams import GRAM_LENGTH
from text_handler import PUNCTUATION, TERMINATOR

class Bot(object):
    """
    Collection of methods to generate a twitter message.
    """
    def __init__(self):
        """
        Initialise the bot.
        """
        self.name = 'MarkovBot'
        self.log = self.name + '.log'
        self.found_matrix_files = matrices.test_for_matrix_files()
        return

    def build_tweet(self, corpus):
        """
        Build the twitter message.
        """
        matrix = matrices.MatrixList(self.found_matrix_files, corpus)
        while True:
            text = Sentence()
            text.ngram = random_start(matrix)
            for word in text.ngram:
                text.add_word(word)
            while text.ngram[GRAM_LENGTH-1] not in TERMINATOR:
                text.ngram = get_next_word(matrix, text.ngram)
                text.add_word(text.ngram[GRAM_LENGTH-1])
            if len(text.text) <= 140:
                return text.text

def random_start(matrix):
    """
    Pick a random starting n-gram.
    """
    start_index = arb_random.get_random_index(matrix.start_prob)
    start_ngram = matrix.get_start_words(start_index)
    return start_ngram

def get_next_word(matrix, last_ngram):
    """
    Get the next word based on the previous n-gram.
    """
    next_word_index = matrix.get_next_index(last_ngram)
    new_ngram = []
    for iword in xrange(len(last_ngram)-1):
        new_ngram.append(last_ngram[iword+1])
    new_ngram.append(matrix.word_list[next_word_index])
    return new_ngram

class Sentence(object):
    """
    Class to manage the twitter message.
    """
    def __init__(self):
        """
        Create an empty message and n-gram.
        """
        self.text = ''
        self.ngram = []
        for iword in xrange(GRAM_LENGTH):
            self.ngram.append('')

    def add_word(self, word):
        """
        Add a new word or punctuation character to the message.
        """
        if word in PUNCTUATION or len(self.text) == 0:
            self.text += word
        else:
            self.text += (' ' + word)
