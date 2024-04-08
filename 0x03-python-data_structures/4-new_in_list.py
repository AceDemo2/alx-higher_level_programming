#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    s = my_list[:]
    if 0 <= idx < len(s):
        s[idx] = element
    return (s)
