#!/usr/bin/python3
def search_replace(my_list, search, replace):
    n = []
    for i in range(len(my_list)):
        if my_list[i] == search:
            n.append(replace)
        else:
            n.append(my_list[i])

