#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        i = 0
        for j in range(x):
            print(my_list[j], end='')
            i += 1
    except Exception:
        pass
    print()
    return i
