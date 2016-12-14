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
