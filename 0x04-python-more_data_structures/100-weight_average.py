#!/usr/bin/python3
def weight_average(my_list=[]):
    num = 0
    denum = 0
    tot = 0
    if my_list:
        for i in my_list:
            num += i[0] * i[1]
            denum += i[1]
        tot = num / denum
    return tot
