#!/usr/bin/python3
"""
Module to stablish tha base class
"""


import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns a JSON string representation of the dictionary"""
        if list_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation of list_objs to a file"""
        list_ret = []
        filename = cls.__name__ + '.json'
        with open(filename, "w") as file:
            if list_objs:
                for obj in list_objs:
                    list_ret.append(obj.to_dictionary())
            file.write(cls.to_json_string(list_ret))

    @staticmethod
    def from_json_string(json_string):
        """Return a list of JSON string representation of json_string"""
        if json_string:
            return (json.loads(json_string))
        return ([])

    @classmethod
    def create(cls, **dictionary):
        """Return an instance with all attribute already set"""
        if cls.__name__ == 'Rectangle':
            dummy = cls(69, 69)
        elif cls.__name__ == 'Square':
            dummy = cls(69)
        cls.update(dummy, **dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Return a list of instance"""
        ret = []
        filename = cls.__name__ + '.json'
        try:
            with open(filename, 'r') as file:
                dict_list = cls.from_json_string(file.read())
        except:
            dict_list = {}
        for obj_dict in dict_list:
            ret.append(cls.create(**obj_dict))
        return ret
