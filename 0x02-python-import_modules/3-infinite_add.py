#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    lent = len(argv)
    add = 0
    for i in range(1, lent):
        add += int(argv[i])
    print(add)
