#!/usr/bin/python3
def no_c(my_string):
    my_string1 = ""
    j = 0
    for i in range(len(my_string)):
        if not 'c' and not 'C':
            my_string1[j] = my_string[i]
            j += 1
    return (my_string1)
