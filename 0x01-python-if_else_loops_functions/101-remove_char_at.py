#!/usr/bin/python3
def remove_char_at(str, n):
    if n < 0:
        return str

    ustr = ''
    for i in range(len(str)):
        if i != n:
            ustr += str[i]

    return ustr
