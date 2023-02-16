#!/usr/bin/python3
"""
    Module to check if an object is exactly a class
"""


def is_same_class(obj, a_class):
    """
    Function that return true if obj is exactly an instance of a_class
    """
    return (type(obj) is a_class)