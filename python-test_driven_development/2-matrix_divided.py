#!/usr/bin/python3
"""
>>> add_integer(5, 9)
14
"""


def matrix_divided(matrix, div):
    """
    >>> add_integer(5, 5)
    10
    """
    """if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")"""
    divided_matrix = []
    for row in matrix:
        divided_matrix.append(list(map(lambda x: round(x / div, 2), row)))
    return divided_matrix
