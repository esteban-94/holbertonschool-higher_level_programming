#!/usr/bin/python3
"""
Module to stablish the Square Class
"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """Square Rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """Class Constructor"""
        super().__init__(size, size, x, y, id)
        self.size = size

    def __str__(self):
        """Function that prints square description"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - "\
               f"{self.height}"

    @property
    def size(self):
        """Definition"""
        return self.__width

    @size.setter
    def size(self, value):
        """Re-definition """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("size must be > 0")
        self.__width = value
