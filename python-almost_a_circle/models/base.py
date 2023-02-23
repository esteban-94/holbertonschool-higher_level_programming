#!/usr/bin/python3
"""
Module to stablish tha base class
"""


class Base:
    """Class Base"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Class Constructor"""
        if id:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def to_json_string(my_obj):
        """returns the JSON representation of an object (string)"""
        import json
        return json.dumps(my_obj)