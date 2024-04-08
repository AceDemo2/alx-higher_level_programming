#!/usr/bin/python3
def no_c(my_string):
    my_string1 = my_string[:]
    for i in my_string1:
        if i == 'c' or i == 'C':
            del i
    return (my_string1)
