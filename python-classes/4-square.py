#!/usr/bin/python3
"""This module have a class that defines a square """


class Square:
    """Definition of square attribute"""
    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        """Definition of square size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Re-definition of square attribute to private"""
        if (isinstance(value, int) is False):
            raise TypeError("size must be an integer")
        elif (value < 0):
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Calcs  and return the area of square"""
        return self.size ** 2
