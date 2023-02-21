#!/usr/bin/python3
"""
Module to stablish the Ractangle Class
"""


Base = __import__('base').Base


class Rectangle(Base):
    """Class Rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Class Constructor"""
        super().__init__(id)

    @property
    def width(self):
        """Definition"""
        return self.__width

    @width.setter
    def width(self, value):
        """Re-definition """
        self.__width = value

    @property
    def height(self):
        """Definition"""
        return self.__height

    @height.setter
    def height(self, value):
        """Re-definition """
        self.__height = value