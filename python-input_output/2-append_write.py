#!/usr/bin/python3
"""
    Module with a writing function
"""


def append_write(filename="", text=""):
    """Writes some text on a file. This doesn't overwrite the content of the
    file"""
    with open(filename, encoding='utf-8', mode='a') as file:
        return file.write(text)
