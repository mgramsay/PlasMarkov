#!/usr/bin/env python

'''
A basic Markov chain bot
'''

import sample_text
import arb_random
import matrices
import ngrams

def get_next_index(last_word, new_word, ngram_list, t_matrix):
    current_ngram = ngrams.build_ngram(last_word, new_word)
    ngram_index = ngram_list.index(current_ngram)
    next_word_index = arb_random.get_random_index(t_matrix.matrix[ngram_index])
    return next_word_index

def main():
    tweet = []
    text_file = 'example_obama.txt'
    full_text = sample_text.read_string_list(text_file)
    ngram_list = sample_text.build_ngram_list(full_text)
    t_matrix, start_ngrams, start_probs, word_list = \
        matrices.build_transition_matrix(full_text, ngram_list)

    remaining_chars = 140
    while remaining_chars > 0:
        sentence = []
        print len(tweet)
        if len(tweet) == 0:
            start_ind = arb_random.get_random_index(start_probs)
            # Pick a random starting n-gram, based on frequency analysis of
            # the sampled text
            last_word, new_word = ngrams.split_ngram(start_ngrams[start_ind])
            sentence.append(last_word)
        else:
            next_word_index = get_next_index(last_word, new_word, ngram_list,
                                             t_matrix)
            # For any sentences after the first, just use the transition matrix
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
            if len(tweet) > 0:
                remaining_chars -= 1
                # Account for spaces between sentences
            tweet.append(to_append)
    if len(tweet) > 1:
        new_tweet = ' '.join(tweet[0:len(tweet)-1])
    else:
        new_tweet = tweet[0]
    print new_tweet

if __name__ == '__main__':
    main()