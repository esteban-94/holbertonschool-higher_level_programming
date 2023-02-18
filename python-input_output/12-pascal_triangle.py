#!/usr/bin/python3
"""
    Great Pascal triangle!!
"""


def pascal_triangle(n):
    """Main function that initializes the triangle array, creates the number
    of internal arrays needed and returns the completed triangle"""
    pascal_tri = []
    for list_row in range(n):
        pascal_tri.append(pascal_row(pascal_tri, list_row))
    return pascal_tri


def pascal_row(pascal_tri, list_row):
    """Auxiliary function that fills the internal arrays that make up the rows
    of the triangle"""
    ret_row = [1]  # here is the initialization of the triangle
    for num in range(len(pascal_tri)):
        ret_row.append(pascal_numb(pascal_tri, list_row, num))
    return ret_row


def pascal_numb(pascal_tri, list_row, num):
    """Auxiliary function that generates the correct numbers that form the
    arrays of the triangle rows"""
    try:
        num = pascal_tri[list_row - 1][num] + pascal_tri[list_row - 1][num + 1]
    except(IndexError):
        num = pascal_tri[list_row - 1][num]
    return num
