#!/usr/bin/python3
"""
    Module to 
"""


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
import sys
import json


try:
    arguments = load_from_json_file("add_item.json")
except Exception:
    arguments = []

for element in range(len(sys.argv)):
    arguments.append(sys.argv[element])

with open("add_item.json", encoding='utf-8', mode='w') as file:
    file.write(json.dumps(arguments))
