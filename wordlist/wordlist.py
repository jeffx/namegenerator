from random import randint
import re

class Wordlist(object):
    def __init__(self, file_name):
        self.file_name = file_name
        self.words = []
        self.match_string = re.compile(r'[^a-z]')
        self._read_words()

    def _cleaner(self, word):
        #word = word.lower()
        word = re.sub(self.match_string, '', word.strip().lower())
        if len(word.strip()) > 5:
            #print word
            return word.strip()
        else:
            return False

    def _read_words(self):
        with open(self.file_name, 'r') as word_file:
            for w in word_file:
                word = re.sub(self.match_string, '', w.strip().lower())
                if len(word) > 5:
                    self.words.append(word)

    def how_many_words(self):
        return len(self.words)

    def get_word(self, number=None):
        if number:
            if number <= self.how_many_words():
                return self.words[number]
            else:
                raise 'foobar'
        else:
            return self.words[randint(0, len(self.words) - 1)]

    def word_to_syllable(self, word):
        syllable_list = []
        vowel_flag = False
        syllable = []
        for letter in word:
            if re.match('a|e|i|o|u', letter):
                if vowel_flag:
                    syllable_list.append(''.join(syllable))
                    syllable = []
                    syllable.append(letter)
                    vowel_flag = True
                else:
                    syllable.append(letter)
                    vowel_flag = True
            else:
                syllable.append(letter)
        syllable_list.append(''.join(syllable))
        return syllable_list
