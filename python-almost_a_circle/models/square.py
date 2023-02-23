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
        return f"[Square] ({self.id}) {self.x}/{self.y} - "\
               f"{self.height}"

    @property
    def size(self):
        """Definition"""
        return self.width

    @size.setter
    def size(self, value):
        """Re-definition """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Function that updates the class attributes"""
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.size = args[1]
            if len(args) >= 3:
                self.x = args[2]
            if len(args) == 4:
                self.y = args[3]
        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)
