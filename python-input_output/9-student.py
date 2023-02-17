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

    def to_json(self):
        """returns the dictionary description with simple data structure"""
        return (self.__dict__)
