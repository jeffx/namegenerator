import re


def word_to_list(word):
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
