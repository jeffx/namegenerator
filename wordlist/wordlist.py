from random import randint

class Wordlist(object):
    def __init__(self, file_name):
        self.file_name = file_name
        self.words = []
        self._read_words()

    def _read_words(self):
        with open(self.file_name, 'r') as word_file:
            self.words = [f.strip() for f in word_file]

    def how_many_words(self):
        return len(self.words)

    def get_word(self, number=None):
        if number:
            if number <= self.how_many_words():
                return self.words[number]
            else:
                raise 'foobar'
        else:
            return self.words[randint(0, len(self.words))]
