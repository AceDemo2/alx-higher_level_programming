#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    for i, j in a_dictionary.items():
        if i == value:
            del i
    return a_dictionary
