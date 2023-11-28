#!/usr/bin/python3
for i in range(100):
    print('{:02n}'.format(i), end=', ' if i < 99 else '\n')
