#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    k = []
    for i, j in a_dictionary.items():
        if j == value:
            k += i
    for l in k:
        del a_dictionary[l]
    return a_dictionary
