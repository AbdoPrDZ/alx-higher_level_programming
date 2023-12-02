#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    """
    delete_at - Delete element in list at position idx
    @my_list: The list want to modify
    @idx: The element position
    Return: The modified list
    """
    mLen = len(my_list)
    if idx < 0 or idx > mLen:
        return my_list

    del my_list[idx]

    return my_list
