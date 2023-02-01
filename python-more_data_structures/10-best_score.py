#!/usr/bin/python3
def best_score(a_dictionary):
    score = 0
    best_student = None
    if a_dictionary:
        for key in a_dictionary:
            if a_dictionary[key] > score:
                best_student = key
                score = a_dictionary[key]
    return best_student
