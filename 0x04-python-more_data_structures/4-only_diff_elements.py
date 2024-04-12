#!/usr/bin/python3
def s(i1, j1):
    k = []
    f = 0
    i = 0
    while i < len(i1):
        j = 0
        while j < len(j1):
            if i1[i] == j1[j]:
                f = 1
                break
            else:
                j += 1
        if f == 0:
            k.append(i1[i])
        else:
            f = 0
        i += 1
    return k
def only_diff_elements(set_1, set_2):
    s1 = s(set_1, set_2)
    s2 = s(set_2, set_1)
    s3 = s1 + s2
    return set(s3)
