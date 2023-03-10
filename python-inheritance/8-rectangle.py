#!/usr/bin/python3
"""
This module have a class for create a rectangle
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle is a child class from BaseGeometry"""

    def __init__(self, width, height):
        """Constructor"""
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height
