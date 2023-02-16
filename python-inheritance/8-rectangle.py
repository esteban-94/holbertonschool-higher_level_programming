#!/usr/bin/python3
"""
This module have a empty class named Geometry
"""


class BaseGeometry:
    """Class description for Base Geometry"""
    
    def area(self):
        """Public instance method that raise an Exception"""
        raise Exception('area() is not implemented')
    
    def integer_validator(self, name, value):
        """Public instance method that validates value"""
        if not type(value) is int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))
        
class Rectangle(BaseGeometry):
    """Rectangle is a child class from BaseGeometry"""
    
    def __init__(self, width, height):
        """Constructor"""
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height