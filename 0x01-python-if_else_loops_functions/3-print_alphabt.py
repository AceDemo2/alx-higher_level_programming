#!/usr/bin/python3
for alpha in range(ord('a'), ord('z') + 1):
    if alpha != ord('e') or alpha != ord('q'):
        print("{}".format(chr(ord(alpha))), end='')
