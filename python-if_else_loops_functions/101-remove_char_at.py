#!/usr/bin/python3
def remove_char_at(str, n):
    if (n >= 0) and (n <= len(str)):
        new_string = ""
        for i in range(len(str)):
            if i != n:
                new_string += str[i]
        return (new_string)
    return (str)
