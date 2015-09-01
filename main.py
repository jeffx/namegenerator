#!/bin/env python
""" Idea for name generator:
        1.  Pick three words from the dictionary
        2.  Break them into syllables
        3.  First name is first syllabel of second word combined with
            first syllable of first syllabel of first word
        4.  Last name is first syllabel of thrid word combined with second
            syllabel of second word
"""
from syllable import syllable

first_word = 'operating'
second_word = 'principles'
third_word = 'technical'
first_syllable = syllable.word_to_list(first_word)
second_syllable = syllable.word_to_list(second_word)
third_syllable = syllable.word_to_list(third_word)
first_name = '{0}{1}'.format(second_syllable[0],
                             first_syllable[0]).capitalize()
second_name = '{0}{1}'.format(third_syllable[0],
                              second_syllable[1]).capitalize()
print '{0} {1}'.format(first_name, second_name)
