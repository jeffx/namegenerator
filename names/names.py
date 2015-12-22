from wordlist.wordlist import Wordlist


class Names(Wordlist):
    default_wordlist = '/home/jeffx/Projects/namegenerator/data/words.dat'

    def __init__(self, word_file=None):
        super(Names, self).__init__(self.default_wordlist)

    def generate_name(self):
        self.first_word = self.get_word()
        self.second_word = self.get_word()
        self.third_word = self.get_word()
        first_syllable = self.word_to_syllable(self.first_word)
        second_syllable = self.word_to_syllable(self.second_word)
        third_syllable = self.word_to_syllable(self.third_word)
        first_name = '{0}{1}'.format(second_syllable[0],
                                     first_syllable[0]).capitalize()
        if len(second_syllable) <= 2:
            second_name = '{0}{1}'.format(third_syllable[0],
                                          first_syllable[0])
        else:
            second_name = '{0}{1}'.format(third_syllable[0],
                                          second_syllable[1]).capitalize()
        return '{0} {1}'.format(first_name, second_name)
