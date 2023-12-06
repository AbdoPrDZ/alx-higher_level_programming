#!/usr/bin/python3
def weight_average(my_list=[]):
    mLen = len(my_list)
    if mLen == 0:
        return 0

    a = 0
    b = 0
    for x, y in my_list:
        a += x * y
        b += y

    return a / (b if b != 0 else 1)
