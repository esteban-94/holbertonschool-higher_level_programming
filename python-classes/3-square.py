#!/usr/bin/python3
"""This module have a class that defines a square """


class Square:
    """Definition of square attribute"""
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif (size < 0):
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """Calcs  and return the area of square"""
        return self.size ** 2
