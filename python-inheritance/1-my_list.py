#!/usr/bin/python3
"""
    This module contains a child class named MyList that inherit from list
"""


class MyList(list):
    """An empty list that inherits the sort method from list class"""

    def __init__(self):
        """Constructor"""
        self.MyList = []

    def print_sorted(self):
        """This function prints a list sorted in ascending order of integers"""
        sorted_list = self[:]
        sorted_list.sort()
        print(sorted_list)
