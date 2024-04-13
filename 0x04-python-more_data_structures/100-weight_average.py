#!/usr/bin/python3
def weight_average(my_list=[]):
    num = 0
    denum = 0
    for i in my_list:
        num += i[0] * i[1]
        denum += i[1]
    return num / denum
