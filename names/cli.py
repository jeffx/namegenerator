import sys

from names.names import Names


def cli():
    names = Names()
    print(names.generate_name())
