#!/usr/bin/python3
"""
    Module with a read function
"""


def read_file(filename=""):
    """Reads a text file using UTF8 encoding"""
    with open(filename, encoding='utf-8') as file:
        print(file.read(), end="")