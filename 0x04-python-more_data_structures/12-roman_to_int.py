#!/usr/bin/python3
def roman_to_int(roman_string):
    sym = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    total = 0
    p = 0
    for i in roman_string:
        v = sym[i]
        if v is None:
            return 0
        if v < p:
            total -= v
        else:
            total += v
            p = v
    return total
