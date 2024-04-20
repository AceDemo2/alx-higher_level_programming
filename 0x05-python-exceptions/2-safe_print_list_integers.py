#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    try:
        i = 0
        for j in range(x):
            print("{:d}".format(my_list[j]), end='')
            i += 1
    except Exception:
        pass
    print()
    return i
