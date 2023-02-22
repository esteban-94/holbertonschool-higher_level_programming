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

    def __str__(self):
        """Function that prints square description"""
        return f"[Square] ({self.id}) {self.__x}/{self.__y} - "\
               f"{self.__width}"
