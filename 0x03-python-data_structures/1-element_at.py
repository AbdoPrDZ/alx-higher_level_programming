#!/usr/bin/python3
def element_at(my_list, idx):
    """
    element_at - Get element from list at position idx
    @my_list: The list want to get element from it
    @idx: The position of element
    Return: The element if exists, or None
    """
    if idx < 0 or idx >= len(my_list):
        return None
    else:
        return my_list[idx]
