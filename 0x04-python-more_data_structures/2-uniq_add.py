#!/usr/bin/python3
def uniq_add(my_list=[]):
    """
    uniq_add - calculate addition of unique items in list
    @my_list: the list
    Return: the some of unique items list
    """
    s = 0
    uniq_list = []
    for item in my_list:
        if not (item in uniq_list):
            s += item
            uniq_list.append(item)

    return s
