#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    le = len(sys.argv)
    pl = "s" if le >= 3 else ""
    si = ":" if le >= 2 or le == 0 else "."
    print("{} argument{}{}".format((le - 1 if le > 0 else 0), pl, si))
    i = 1
    while i < le:
        print("{}: {}".format(i, sys.argv[i]))
        i += 1
