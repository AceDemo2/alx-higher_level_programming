#!/usr/bin/python3
def print_last_digit(number):
    last = (-number if number < 0 else number) % 10
    print(last, end='')
    return (last)
