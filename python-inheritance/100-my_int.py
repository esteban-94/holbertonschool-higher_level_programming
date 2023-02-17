#!/usr/bin/python3
"""
    This module contains a class that inherits from int
"""


class MyInt(int):
    """MyInt inherits from int"""

    def __init__(self, number):
        """Constructor"""
        self.number = number

    def __eq__(self, other):
        """Define the == comparision"""
        return self.number != other

    def __ne__(self, other):
        """Define the != comparison"""
        return self.number == other
