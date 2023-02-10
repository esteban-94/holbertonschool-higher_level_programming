#!/usr/bin/python3
'''this module will be testing by 0-add-integer.txt'''


def add_integer(a, b=98):
    '''This function sum two integers.'''

    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
