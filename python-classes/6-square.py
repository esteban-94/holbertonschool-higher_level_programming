#!/usr/bin/python3
"""This module have a class that defines a square """


class Square:
    """Definition of square attribute"""
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    @property
    def size(self):
        """Definition of square size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Re-definition of square size attribute to private"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif (value < 0):
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """Definition of square position"""
        return self.__position

    @position.setter
    def position(self, value):
        """Re-definition of square position attribute to private"""
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """Calcs  and return the area of square"""
        return self.size ** 2

    def my_print(self):
        """Prints a square with # symbol"""
        if self.size == 0:
            print('')
        for i in range(self.size):
            print('#' * self.size)
