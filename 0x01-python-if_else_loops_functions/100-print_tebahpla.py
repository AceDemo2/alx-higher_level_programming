#!/usr/bin/python3
for alpha in range(ord('z'), ord('a') - 1, -1):
    if ord('A') <= ord(alpha) >= ord('Z'):
        alpha = chr((ord(alpha) - 32))
    print('{}'.format(chr(alpha)), end='')
