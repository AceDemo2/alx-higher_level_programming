#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    le = len(sys.argv)
    if le <= 0:
        print("0 arguments.")
    else:
        print("{} arguments:".format(le))
        i = 1
        while i <= le:
            print("{} {}".format(i, argv[i]))
            i += 1
