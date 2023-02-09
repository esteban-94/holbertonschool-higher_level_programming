#!/usr/bin/python3
"""
>>> add_integer(5, 9)
14
"""


def add_integer(a, b=98):
    """
    >>> add_integer(5, 5)
    10
    """

    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
