#!/usr/bin/python3
"""
    Module to create from JSON
"""


def load_from_json_file(filename):
    """creates an object from a JSON file"""

    import json
    with open(filename, encoding='utf-8') as file:
        return json.load(file)