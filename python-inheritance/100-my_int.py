#!/usr/bin/python3
"""
    This module contains a 
"""


class MyInt(int):
    """
    MyInt
    """

    def __init__(self):
        """Constructor"""
        self.MyInt = 0

    def __eq__(self, other):
        """Define the == comparision"""
        return self != other

    def __ne__(self, other):
        """Define the != comparison"""
        return self == other