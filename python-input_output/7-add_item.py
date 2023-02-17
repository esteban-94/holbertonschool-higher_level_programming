#!/usr/bin/python3
'''Adds all arguments to a Python list,\
     and then save them to a file'''
import json
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

try:
    arguments = load_from_json_file("add_item.json")
except:
    arguments = []

for i in sys.argv[1:]:
    arguments.append(i)
save_to_json_file(arguments, "add_item.json")
