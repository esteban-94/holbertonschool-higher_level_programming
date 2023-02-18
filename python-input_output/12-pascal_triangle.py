#!/usr/bin/python3
"""
    Great Pascal triangle!!
"""


def pascal_triangle(n):
    """Def funct"""
    pascal_tri = []
    for list_row in range(n):
        pascal_tri.append(pascal_row(pascal_tri, list_row))
    return pascal_tri

def pascal_row(pascal_tri, list_row):
    """Def funct"""
    ret_row = [1]
    for num in range(len(pascal_tri)):
        ret_row.append(pascal_numb(pascal_tri, list_row, num))
    return ret_row

def pascal_numb(pascal_tri, list_row, num):
    """Def funct"""
    if list_row == 1:
        return 1
    try:
        num = pascal_tri[list_row - 1][num] + pascal_tri[list_row - 1][num + 1]
    except(IndexError):
        num = pascal_tri[list_row - 1][num]
    return num