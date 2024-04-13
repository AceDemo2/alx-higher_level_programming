#!/usr/bin/python3i
def best_score(a_dictionary):
    i = 0
    k = ""
    for j in a_dictionary:
        if a_dictionary[j] > i:
            i = a_dictionary[j]
            k = j
    return k
