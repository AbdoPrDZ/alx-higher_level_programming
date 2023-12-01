#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    """
    replace_in_list - Replace element of list at idx
    @my_list: The list want to replace his element
    @idx: The position of the element
    Return: The modified list
    """
    if not (idx < 0 or idx >= len(my_list)):
        my_list[idx] = element
    return my_list
