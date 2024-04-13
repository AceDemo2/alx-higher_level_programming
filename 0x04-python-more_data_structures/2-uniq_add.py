#!/usr/bin/python3
def uniq_add(my_list=[]):
    n = set(my_list)
    j = 0
    for i in n:
        j += i
    return (j)
