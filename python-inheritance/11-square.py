#!/usr/bin/python3
"""
This module have a class for create a square
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square is a child class from Rectangle"""

    def __init__(self, size):
        """Constructor"""
        super().integer_validator("size", size)
        self.__size = size

    def area(self):
        """This funct return the area of the square"""
        return self.__size ** 2

    def __str__(self):
        """Function that prints square description"""
        return f"[Square] {self.__size}/{self.__size}"
