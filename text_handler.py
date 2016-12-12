PUNCTUATION = (',', '.', '?', '!', ':', ';')
TERMINATOR = ('.', '?', '!')

def read_corpus(corpus_file):
    global PUNCTUATION
    file_id = open(corpus_file, 'r')
    corpus_text = file_id.read()
    file_id.close()
    
    strings = corpus_text.split()
    full_text = []
    for word in strings:
        if word.endswith(PUNCTUATION):
            full_text.append(word[0:len(word)-1])
            full_text.append(word[len(word)-1])
        else:
            full_text.append(word)
    return full_text
