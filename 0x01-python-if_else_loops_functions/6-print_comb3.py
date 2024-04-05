#!/usr/bin/python3
for num in range(10):
    for num2 in range(10):
        if num == 8 and num2 == 9:
            print("{}{}".format(num), end='')
        elif num2 > num and num != num2:
            print("{}{}, ".format(num2), end='')
