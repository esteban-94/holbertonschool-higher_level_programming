#!/usr/bin/python3
"""
    Module with student class
"""


class Student():
    """Student class with student information"""

    def __init__(self, first_name, last_name, age):
        """Constructor"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """returns the dictionary description with simple data structure"""
        if attrs and all(type(attr) is str for attr in attrs) or attrs == []:
            returned_dict = {}
            for key, value in self.__dict__.items():
                for attr in attrs:
                    if key == attr:
                        returned_dict[key] = value
            return returned_dict
        return self.__dict__
