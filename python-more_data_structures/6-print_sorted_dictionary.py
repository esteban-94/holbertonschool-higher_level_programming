#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sorted_keys = sorted(list(a_dictionary))
    for key in sorted_keys:
        print("{:s}: {}".format(key, a_dictionary[key]))
