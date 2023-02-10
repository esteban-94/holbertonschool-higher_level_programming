#!/usr/bin/python3
"""This module have a class that defines a rectangle """


class Rectangle:
    """Definition of rectangle attribute"""
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """Definition of rectangle width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Re-definition of rectangle width attribute to private"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif (value < 0):
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Definition of rectangle height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Re-definition of rectangle height attribute to private"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif (value < 0):
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """Calcs  and return the area of rectangle"""
        return self.width * self.height

    def perimeter(self):
        """Calcs  and return the perimeter of rectangle"""
        if self.width != 0 and self.height != 0:
            return self.width * 2 + self.height * 2
        else:
            return 0
