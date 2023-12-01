#!/usr/bin/python3
def max_integer(my_list=[]):
    """
    max_integer - Find the bigger integer on list
    @my_list: The list we want to search inside
    Return: the bigger integer
    """
    mLen = len(my_list)
    if mLen == 0:
        return None

    m = my_list[0]

    for i in range(1, mLen):
        n = my_list[i]
        if n > m:
            m = n

    return m
