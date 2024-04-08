#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if my_list != None:
        s = my_list[::-1]
        for i in s:
            print("{:d}".format(i))
