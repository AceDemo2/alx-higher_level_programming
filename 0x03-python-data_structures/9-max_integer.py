#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list:
        i = my_list[0]
        for j in my_list:
            if j > i:
                i = j
        return (i)
    else:
        return (None)
