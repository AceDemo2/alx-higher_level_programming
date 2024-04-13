#!/usr/bin/python3i
def best_score(a_dictionary):
    i = 0
    for j in a_dictionary:
        if a_dictionary[j] > i:
            i = a_dictionary[j]
    return i
