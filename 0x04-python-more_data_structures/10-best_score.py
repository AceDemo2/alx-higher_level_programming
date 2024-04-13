#!/usr/bin/python3i
def best_score(a_dictionary):
    i = a_dictionary(list(a_dictionary))[0]
    k = ""
    if a_dictionary:
        for j in a_dictionary:
            if a_dictionary[j] > i:
                i = a_dictionary[j]
                k = j
        return k
    return None
