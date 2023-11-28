#!/usr/bin/python3
def uppercase(str):
    ustr = ''
    for c in str:
        if ord(c) >= ord('a') and ord(c) <= ord('z'):
            ustr = '{0}{1}'.format(ustr, chr(ord(c) - 32))
        else:
            ustr += c
    print(ustr)
