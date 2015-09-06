#!/bin/env python
from names.names import Names

import sys
""" Idea for name generator:
        1.  Pick three words from the dictionary
        2.  Break them into syllables
        3.  First name is first syllabel of second word combined with
            first syllable of first syllabel of first word
        4.  Last name is first syllabel of thrid word combined with second
            syllabel of second word
"""


count = 0
names = Names()

#while count < 100000:
while True:
    print names.generate_name()
    count = count + 1
