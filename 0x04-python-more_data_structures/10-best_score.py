#!/usr/bin/python3i
def best_score(a_dictionary):
    if a_dictionary:
        ls = list(a_dictionary)
        k = ls[0]
        value = a_dictionary[k]
        for j in a_dictionary:
            if a_dictionary[j] > value:
                value = a_dictionary[j]
                k = j
        return k
    return None
