#!/usr/bin/python3
def roman_to_int(roman_string):
    sym = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    total = 0
    i = 0
    p = 0
    for s, v in sym.items():
        if s == roman_string[i]:
            if v < p:
                total += v
            else:
                total -= 2 * p
            p = v
            i += 1
        else:
            return 0
    return total

