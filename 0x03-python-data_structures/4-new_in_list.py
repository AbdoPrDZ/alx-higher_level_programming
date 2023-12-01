#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    """
    new_in_list - Replace list element at idx in new list
    @my_list: The original list
    @idx: The position of element
    @element: The new element
    Return: The new replaced list
    """
    cList = [*my_list]
    if not (idx < 0 or idx >= len(my_list)):
        cList[idx] = element
    return cList
