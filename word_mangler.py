#!/usr/bin/env python
import re
with open('./data/words', 'r') as word_file:
    for word in word_file:
        word = word.strip()
        word = word.lower()
        word = re.sub(r'[^a-zA-Z]', '', word)
        if len(word.strip()) > 5:
            print word

