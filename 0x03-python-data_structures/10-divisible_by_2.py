#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    j = []
    k = [True, False]
    for i in my_list:
        if i % 2 == 0:
            j += k[0]
        else:
            j += k[1]
    return (j)
