#!/usr/bin/python3
import sys
argc = len(sys.argv)
s = 0
for i in range(1, argc):
    n = int(sys.argv[i])
    s += n
print('{}'.format(s))
