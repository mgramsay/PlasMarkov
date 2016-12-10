#!/usr/bin/env python

'''
A basic Markov chain bot
'''

import sys

import sample_text
import arb_random
import matrices
import ngrams

def get_next_index(last_word, new_word, ngram_list, t_matrix):
    current_ngram = ngrams.build_ngram(last_word, new_word)
    ngram_index = ngram_list.index(current_ngram)
    if sum(t_matrix.matrix[ngram_index]) < 0.5:
        return -1
    next_word_index = arb_random.get_random_index(t_matrix.matrix[ngram_index])
    return next_word_index

def random_start(start_ngrams, start_probs):
    '''
    Pick a random starting n-gram, based on frequency analysis of the sampled
    text
    '''
    start_ind = arb_random.get_random_index(start_probs)
    last_word, new_word = ngrams.split_ngram(start_ngrams[start_ind])
    return last_word, new_word

def main(corpus):
    tweet = []
    found_matrix_files = matrices.test_for_matrix_files()
    if found_matrix_files and not corpus:
        start_ngrams, start_probs = matrices.read_start_matrix()
        t_matrix, word_list, ngram_list = \
            matrices.read_transition_matrix()
    else:
        if not corpus:
            print 'No matrix files found, and no corpus provided.'
            print 'Running using the contents of example.txt'
            print ''
            corpus = 'example.txt'
        full_text = sample_text.read_string_list(corpus)
        ngram_list = sample_text.build_ngram_list(full_text)
        t_matrix, start_ngrams, start_probs, word_list = \
            matrices.build_transition_matrix(full_text, ngram_list)

    remaining_chars = 140
    while remaining_chars > 0:
        sentence = []
        if len(tweet) == 0:
            last_word, new_word = random_start(start_ngrams, start_probs)
            sentence.append(last_word)
        else:
            next_word_index = get_next_index(last_word, new_word, ngram_list,
                                             t_matrix)
            # For any sentences after the first, just use the transition matrix
            if next_word_index == -1:
                last_word, new_word = random_start(start_ngrams, start_probs)
                if last_word not in ngrams.PUNCTUATION:
                    sentence.append(' ')
                sentence.append(last_word)
            else:
                last_word = new_word
                new_word = word_list[next_word_index]
        if new_word not in ngrams.PUNCTUATION:
            sentence.append(' ')
        sentence.append(new_word)
        while new_word not in ngrams.TERMINATOR:
            next_word_index = get_next_index(last_word, new_word, ngram_list,
                                             t_matrix)
            last_word = new_word
            new_word = word_list[next_word_index]
            if new_word not in ngrams.PUNCTUATION:
                sentence.append(' ')
            sentence.append(new_word)
        to_append = ''.join(sentence)
        if len(to_append) <= 140:
            remaining_chars -= len(to_append)
            tweet.append(to_append)
    if len(tweet) > 1:
        new_tweet = ''.join(tweet[0:len(tweet)-1])
    else:
        new_tweet = tweet[0]
    print new_tweet

if __name__ == '__main__':
    corpus = None
    if len(sys.argv) > 1:
        corpus = sys.argv[1]
    main(corpus)
