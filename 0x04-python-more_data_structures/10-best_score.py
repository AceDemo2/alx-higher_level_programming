#!/usr/bin/python3i
def best_score(a_dictionary):
    if a_dictionary:
        l = list(a_dictionary)
        k = l[0]
        i = a_dictionary[k]
        for j in a_dictionary:
            if a_dictionary[j] > i:
                i = a_dictionary[j]
                k = j
        return k
    return None
