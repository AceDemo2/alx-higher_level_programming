#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    s = my_list
    s[idx] = element
    for i in s:
        print("{}".format(i))
