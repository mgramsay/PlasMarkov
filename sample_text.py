'''
Reads sample text file and produces list of the words and n-grams.
'''


import ngrams

def read_string_list(sample_file):
    txt_file = open(sample_file, 'r')
    sample_text = txt_file.read()
    txt_file.close()

    string_list = sample_text.split()
    full_text = []
    for word in string_list:
        if word.endswith(ngrams.PUNCTUATION):
            full_text.append(word[0:len(word)-1])
            full_text.append(word[len(word)-1])
        else:
            full_text.append(word)
    return full_text

def build_ngram_list(full_text):
    ngram_list = []
    for iword in xrange(len(full_text)-1):
        new_ngram = ngrams.build_ngram(full_text[iword], full_text[iword+1])
        if new_ngram not in ngram_list:
            ngram_list.append(new_ngram)
    return ngram_list

