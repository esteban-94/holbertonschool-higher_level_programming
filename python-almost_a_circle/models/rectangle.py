#!/usr/bin/python3
"""
Module to stablish the Ractangle Class
"""


from base import Base


class Rectangle(Base):
    """Class Rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Class Constructor"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

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

    @property
    def x(self):
        """Definition"""
        return self.__x

    @x.setter
    def x(self, value):
        """Re-definition """
        self.__x = value

    @property
    def y(self):
        """Definition"""
        return self.__y

    @y.setter
    def y(self, value):
        """Re-definition """
        self.__y = value