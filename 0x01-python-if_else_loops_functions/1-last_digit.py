#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    num = -number
last = num % 10
if last > 5:
    strn = "and is greater than 5"
elif last == 0:
    strn = "and is 0"
elif last < 6 and last != 0:
    strn = "and is less than 6 and not 0"
print("Last digit of", number, "is", last, strn)
