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
        elif value < 0:
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
        elif value < 0:
            self.val_error_2("y")
        self.__y = value

    def sint_error_all(self, attr):
        """Aux function """
        raise TypeError(f"{attr} must be an integer")

    def val_error_1(self, attr):
        """Aux function """
        raise ValueError(f"{attr} must be > 0")

    def val_error_2(self, attr):
        """Aux function """
        raise ValueError(f"{attr} must be >= 0")

    def area(self):
        """Function that returns Rectangle's Area"""
        return self.width * self.height

    def display(self):
        """Prints a rectangle with # character"""
        for i in range(self.y):
            print('')
        for i in range(self.height):
            print(' ' * self.x + '#' * self.width)

    def __str__(self):
        """Function that prints rectangle description"""
        return f"[Rectangle] ({self.id}) {self.__x}/{self.__y} - "\
               f"{self.__width}/{self.__height}"

    def update(self, *args, **kwargs):
        """Function that updates the class attributes"""
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.width = args[1]
            if len(args) >= 3:
                self.height = args[2]
            if len(args) >= 4:
                self.x = args[3]
            if len(args) == 5:
                self.y = args[4]
        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Dictionaty representation"""
        return {
            'id': self.id,
            'width': self.width,
            'height': self.height,
            'x': self.x,
            'y': self.y
        }
