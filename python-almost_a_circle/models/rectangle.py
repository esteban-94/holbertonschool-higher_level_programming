#!/usr/bin/python3
"""
Module to stablish the Ractangle Class
"""


from models.base import Base


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
        if not isinstance(value, int):
            self.sint_error_all("width")
        elif value <= 0:
            self.val_error_1("width")
        self.__width = value

    @property
    def height(self):
        """Definition"""
        return self.__height

    @height.setter
    def height(self, value):
        """Re-definition """
        if not isinstance(value, int):
            self.sint_error_all("height")
        elif value <= 0:
            self.val_error_1("height")
        self.__height = value

    @property
    def x(self):
        """Definition"""
        return self.__x

    @x.setter
    def x(self, value):
        """Re-definition """
        if not isinstance(value, int):
            self.sint_error_all("x")
        elif value <= 0:
            self.val_error_2("x")
        self.__x = value

    @property
    def y(self):
        """Definition"""
        return self.__y

    @y.setter
    def y(self, value):
        """Re-definition """
        if not isinstance(value, int):
            self.sint_error_all("y")
        elif value <= 0:
            self.val_error_2("y")
        self.__x = value

    def sint_error_all(self, attr):
        raise TypeError(f"{attr} must be an integer")

    def val_error_1(self, attr):
        raise ValueError(f"{attr} must be > 0")

    def val_error_2(self, attr):
        raise ValueError(f"{attr} must be >= 0")
