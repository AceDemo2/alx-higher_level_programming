#!/usr/bin/python3
for alpha in range(ord('a'), ord('z') + 1):
    if ord('A') <= ord(alpha) >= ord('Z'):
        alpha = chr((ord(alpha) - 32))
    print(f'{}', alpha, end='')
