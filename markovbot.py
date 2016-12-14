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

import arb_random
import matrices
from text_handler import PUNCTUATION, TERMINATOR

class bot():
    def __init__(self):
        self.name = 'MarkovBot'
        self.log = self.name + '.log'
        self.found_matrix_files = matrices.test_for_matrix_files()
        return

    def build_tweet(self, corpus):
        text = []
        matrix = matrices.matrix_list(self.found_matrix_files, corpus)
        remaining_chars = 140
        random_start = True
        last_ngram = ['', '']
        while remaining_chars > 0:
            sentence, last_ngram = self.build_new_sentence(matrix,
                                                           random_start,
                                                           last_ngram)
            if len(sentence) <= 140:
                remaining_chars -= len(sentence)
                text.append(sentence)
                random_start = False
        if len(text) > 1:
            tweet = ''.join(text[0:len(text)-1])
        else:
            tweet = text[0]
        return tweet

    def build_new_sentence(self, matrix, random_start, last_ngram):
        sentence = []
        last_word = last_ngram[0]
        new_word = last_ngram[1]
        if random_start:
            start_index = arb_random.get_random_index(matrix.start_prob)
            last_word, new_word = matrix.get_start_words(start_index)
            sentence.append(last_word)
        else:
            next_word_index = matrix.get_next_index(last_word, new_word)
            if next_word_index == -1:
                start_index = arb_random.get_random_index(matrix.start_prob)
                last_word, new_word = matrix.get_start_words(start_index)
                if last_word not in PUNCTUATION:
                    sentence.append(' ')
                sentence.append(last_word)
            else:
                last_word = new_word
                new_word = matrix.word_list[next_word_index]
        if new_word not in PUNCTUATION:
            sentence.append(' ')
        sentence.append(new_word)
        while new_word not in TERMINATOR:
            next_word_index = matrix.get_next_index(last_word, new_word)
            last_word = new_word
            new_word = matrix.word_list[next_word_index]
            if new_word not in PUNCTUATION:
                sentence.append(' ')
            sentence.append(new_word)
        return ''.join(sentence), [last_word, new_word]
