#!/usr/bin/python3
for alpha in range(ord('a'), ord('z')):
    if alpha != ord('e') or alpha != ord('q'):
        print(chr(ord(alpha)), end='')
