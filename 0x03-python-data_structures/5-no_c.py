#!/usr/bin/python3
def no_c(my_string):
    """
    no_c - Remove all c and C characters from string
    @my_string: The string want to modify
    Return: The modified string
    """
    nStr = ''

    for c in my_string:
        if c != 'c' and c != 'C':
            nStr += c

    return nStr
