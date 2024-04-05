#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        l = -(-number % 10)
    else:
        l = number % 10
    print(l)
