#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    j = []
    for i in my_list:
        if i % 2 == 0:
            j += True
        else:
            j += False
    return (j)
