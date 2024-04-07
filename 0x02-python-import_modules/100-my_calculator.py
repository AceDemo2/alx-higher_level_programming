#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    from sys import argv
    lent = len(argv)
    if lent != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    a = int(argv[1])
    b = int(argv[3])
    op = argv[2]
    s = [(add, "+"), (sub, "-"), (mul, "*"), (div, "/")]
    i = 0
    j = 1
    while i < len(s):
        if op == s[i][j]:
            r = s[i][0](a,b)
            print("{} {} {} = {}".format(a, op, b, r))
            break
        else:
            i += 1
    else:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
