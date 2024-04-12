#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    unique_elements = []
    for element in set_1:
        if element not in set_2:
            unique_elements.append(element)
    for element in set_2:
        if element not in set_1:
            unique_elements.append(element)
    return set(unique_elements)

