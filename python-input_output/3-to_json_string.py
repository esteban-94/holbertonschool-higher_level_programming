#!/usr/bin/python3
"""
    Module with JSON representation.
"""


def to_json_string(my_obj):
    """returns the JSON representation of an object (string)"""
    import json
    return json.dumps(my_obj)
