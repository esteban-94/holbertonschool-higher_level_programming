#!/usr/bin/python3
"""
This module contains a function call lookup that returns a list of availables
attributes and methods of an object
"""


def lookup(obj):
    """This function returns a list of availables attributes and methos of an
    object"""

    return dir(obj)
