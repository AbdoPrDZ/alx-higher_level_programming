#!/usr/bin/python3
for i in range(25, -1, -1):
    print('{}'.format(chr(ord('A' if i % 2 == 0 else 'a') + i)), end='')
