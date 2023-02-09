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
    if type(matrix) is not list:
        raise TypeError('matrix must be a matrix (list of lists) of integers/floats')

    if type(div) not in [int, float]:
        raise TypeError('div must be a number')

    if div == 0:
        raise ZeroDivisionError('division by zero')
    divided_matrix = []
    for row in matrix:
        divided_matrix.append(list(map(lambda x: round(x / div, 2), row)))
    return divided_matrix
