'''
Constructs the transition matrix
'''

import os

import ngrams

START_FILE = 'start_matrix.txt'
MATRIX_FILE = 't_matrix.txt'

def build_transition_matrix(full_text, ngram_list):
    start_ngrams, start_probs, word_list = build_unique_word_list(full_text)
    t_matrix = transition_matrix(num_ngrams=len(ngram_list),
                                 num_words=len(word_list))
    t_matrix.populate(full_text, ngram_list, word_list)
    t_matrix.save(ngram_list, word_list)
    save_starts(start_ngrams, start_probs)
    return t_matrix, start_ngrams, start_probs, word_list

def test_for_matrix_files():
    found_start_matrix = False
    found_t_matrix = False
    if os.path.isfile(START_FILE):
        found_start_matrix = True
    if os.path.isfile(MATRIX_FILE):
        found_t_matrix = True
    return found_start_matrix and found_t_matrix

def read_start_matrix():
    start_ngrams = []
    start_probs = []
    read_file = open('start_matrix.txt', 'r')
    for line in read_file:
        new_line = line.rstrip().rpartition(' ')
        start_ngrams.append(new_line[0])
        start_probs.append(float(new_line[2]))
    read_file.close()
    return start_ngrams, start_probs

def read_transition_matrix():
    word_list = []
    ngram_list = []
    prob_matrix = []
    read_file = open('t_matrix.txt', 'r')
    word_list = read_file.readline().split()
    num_words = len(word_list)
    for line in read_file:
        new_line = line.split()
        prob_list = new_line[len(new_line)-num_words:len(new_line)]
        matrix_row = []
        for prob in prob_list:
            matrix_row.append(float(prob))
        prob_matrix.append(matrix_row)
        new_ngram = ' '.join(new_line[0:len(new_line)-num_words])
        ngram_list.append(new_ngram)
    read_file.close()
    t_matrix = transition_matrix(num_ngrams=len(ngram_list),
                                 num_words=num_words)
    t_matrix.matrix = prob_matrix
    return t_matrix, word_list, ngram_list

def build_unique_word_list(full_text):
    '''
    Builds a list of the words which appear in the full text. To save time,
    the list of starting n-grams is also built, along with their
    probabilities.
    '''
    start_ngrams = []
    start_probs = []
    word_list = []
    new_sentence = True
    for iword in xrange(len(full_text)):
        word = full_text[iword]
        if word not in word_list:
            word_list.append(word)
            # Add new words to the word list
        if new_sentence:
            new_start = ngrams.build_ngram(word, full_text[iword+1])
            if new_start not in start_ngrams:
                start_ngrams.append(new_start)
                start_probs.append(1.0)
            else:
                start_probs[start_ngrams.index(new_start)] += 1.0
            new_sentence = False
        if word in ngrams.TERMINATOR:
            new_sentence = True
    recip_num_starts = 1.0 / sum(start_probs)
    for iword in xrange(len(start_probs)):
        start_probs[iword] *= recip_num_starts
        # Convert the counts to a probability distribution
    return start_ngrams, start_probs, word_list

def save_starts(start_ngrams, start_probs):
    save_file = open('start_matrix.txt', 'w')
    for ingram in xrange(len(start_ngrams)):
        save_file.write(start_ngrams[ingram])
        save_file.write(' ')
        save_file.write(str(start_probs[ingram]))
        save_file.write('\n')
    save_file.close()

class transition_matrix(object):
    def __init__(self, num_ngrams=1, num_words=1):
        '''
        Create an empty transition matrix
        '''
        self.matrix = []
        for ingram in xrange(num_ngrams):
            word_count = []
            for iword in xrange(num_words):
                word_count.append(0.0)
            self.matrix.append(word_count)

    def __str__(self):
        '''
        Print the transition matrix
        '''
        for ingram in xrange(len(self.matrix)-1):
            print str(self.matrix[ingram])
        return str(self.matrix[len(self.matrix)-1])

    def populate(self, full_text, ngram_list, word_list):
        '''
        Populate the transition matrix
        '''
        for iword in xrange(len(full_text)-2):
            current_ngram = ngrams.build_ngram(full_text[iword], full_text[iword+1])
            ingram = ngram_list.index(current_ngram)
            next_word = word_list.index(full_text[iword+2])
            self.matrix[ingram][next_word] += 1.0
        for ingram in xrange(len(self.matrix)):
            recip_num_words = sum(self.matrix[ingram])
            if recip_num_words > 0.0:
                # Catch potential divide by zero
                recip_num_words = 1.0 / recip_num_words
            for iword in xrange(len(self.matrix[ingram])):
                self.matrix[ingram][iword] *= recip_num_words
                # Normalise each row of the matrix

    def save(self, ngram_list, word_list):
        save_file = open('t_matrix.txt', 'w')
        save_line = ' '.join(word_list)
        save_file.write(save_line)
        save_file.write('\n')
        for ingram in xrange(len(ngram_list)):
            prob_list = []
            for iword in xrange(len(self.matrix[ingram])):
                prob_list.append(str(self.matrix[ingram][iword]))
            save_line = ' '.join(prob_list)
            save_file.write(ngram_list[ingram])
            save_file.write(' ')
            save_file.write(save_line)
            save_file.write('\n')
        save_file.close()

