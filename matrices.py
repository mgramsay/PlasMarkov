'''
Constructs the transition matrix
'''

import os

import arb_random
import ngrams
import text_handler

START_FILE = 'start_matrix.txt'
MATRIX_FILE = 't_matrix.txt'

def test_for_matrix_files():
    found_start_matrix = False
    found_t_matrix = False
    if os.path.isfile(START_FILE):
        found_start_matrix = True
    if os.path.isfile(MATRIX_FILE):
        found_t_matrix = True
    return found_start_matrix and found_t_matrix

class matrix_list():
    def __init__(self, found_matrix_files, corpus_file):
        self.t_matrix = []
        self.word_list = []
        self.ngram_list = []
        self.start_list = []
        self.start_prob = []
        if found_matrix_files and not corpus_file:
            self.load_matrices()
        else:
            if not corpus_file:
                corpus_file = 'example.txt'
            self.build_matrices(corpus_file)
            self.save_matrices()
            
    def load_matrices(self):
        self.read_start_matrix()
        self.read_tmatrix()

    def read_start_matrix(self):
        read_file = open(START_FILE, 'r')
        for line in read_file:
            new_line = line.rstrip().rpartition(' ')
            self.start_list.append(new_line[0])
            self.start_prob.append(float(new_line[2]))
        read_file.close()

    def read_tmatrix(self):
        read_file = open(MATRIX_FILE, 'r')
        self.word_list = read_file.readline().split()
        num_words = len(self.word_list)
        prob_matrix = []
        for line in read_file:
            new_line = line.split()
            prob_list = new_line[len(new_line)-num_words:len(new_line)]
            matrix_row = []
            for prob in prob_list:
                matrix_row.append(float(prob))
            prob_matrix.append(matrix_row)
            new_ngram = ' '.join(new_line[0:len(new_line)-num_words])
            self.ngram_list.append(new_ngram)
        read_file.close()
        self.initialise_tmatrix()
        self.t_matrix = prob_matrix
        
    def build_matrices(self, corpus_file):
        corpus_text = text_handler.read_corpus(corpus_file)
        self.build_ngram_list(corpus_text)
        self.build_string_lists(corpus_text)
        self.build_tmatrix(corpus_text)

    def build_ngram_list(self, corpus_text):
        for iword in xrange(len(corpus_text)-1):
            new_ngram = ngrams.ngram((corpus_text[iword],
                                      corpus_text[iword+1]))
            if new_ngram.ngram not in self.ngram_list:
                self.ngram_list.append(new_ngram.ngram)

    def build_string_lists(self, corpus_text):
        new_sentence = True
        for iword in xrange(len(corpus_text)):
            word = corpus_text[iword]
            if word not in self.word_list:
                self.word_list.append(word)
            if new_sentence:
                new_start = ngrams.ngram((word, corpus_text[iword+1]))
                if new_start.ngram not in self.start_list:
                    self.start_list.append(new_start.ngram)
                    self.start_prob.append(1.0)
                else:
                    i_ngram = self.start_list.index(new_start.ngram)
                    self.start_prob[i_ngram] += 1.0
                new_sentence = False
            if word in text_handler.TERMINATOR:
                new_sentence = True
        recip_num_starts = 1.0 / sum(self.start_prob)
        for iword in xrange(len(self.start_prob)):
            self.start_prob[iword] *= recip_num_starts

    def build_tmatrix(self, corpus_text):
        self.initialise_tmatrix()
        for iword in xrange(len(corpus_text)-2):
            current = ngrams.ngram((corpus_text[iword],
                                   corpus_text[iword+1]))
            i_ngram = self.ngram_list.index(current.ngram)
            next_word = self.word_list.index(corpus_text[iword+2])
            self.t_matrix[i_ngram][next_word] += 1.0
        for i_ngram in xrange(len(self.t_matrix)):
            recip_num_words = sum(self.t_matrix[i_ngram])
            if recip_num_words > 0.0:
                recip_num_words = 1.0 / recip_num_words
            for iword in xrange(len(self.t_matrix[i_ngram])):
                self.t_matrix[i_ngram][iword] *= recip_num_words

    def initialise_tmatrix(self):
        self.t_matrix = []
        for i_ngram in xrange(len(self.ngram_list)):
            word_count = []
            for iword in xrange(len(self.word_list)):
                word_count.append(0.0)
            self.t_matrix.append(word_count)

    def save_matrices(self):
        save_file = open(START_FILE, 'w')
        for istart in xrange(len(self.start_list)):
            save_file.write(self.start_list[istart] + ' ' +
                            str(self.start_prob[istart]) + '\n')
        save_file.close()
        
        save_file = open(MATRIX_FILE, 'w')
        save_line = ' '.join(self.word_list)
        save_file.write(save_line + '\n')
        for i_ngram in xrange(len(self.ngram_list)):
            prob_list = []
            for iword in xrange(len(self.word_list)):
                prob_list.append(str(self.t_matrix[i_ngram][iword]))
            save_line = ' '.join(prob_list)
            save_file.write(self.ngram_list[i_ngram] + ' ' +
                            save_line + '\n')
        save_file.close()

    def get_start_words(self, start_index):
        current = ngrams.ngram((self.start_list[start_index], ''))
        return current.split()

    def get_next_index(self, last_word, new_word):
        current = ngrams.ngram((last_word, new_word))
        ngram_index = self.ngram_list.index(current.ngram)
        if sum(self.t_matrix[ngram_index]) < 0.5:
            return -1
        else:
            return arb_random.get_random_index(self.t_matrix[ngram_index])
