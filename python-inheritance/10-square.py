#!/usr/bin/python3
"""
This module have a empty class named Geometry
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square is a child class from Rectangle"""

    def __init__(self, size):
        """Constructor"""
        self.__size = size
        super().integer_validator("size", size)

    def area(self):
        """This funct return the area of the square"""
        return self.__size ** 2