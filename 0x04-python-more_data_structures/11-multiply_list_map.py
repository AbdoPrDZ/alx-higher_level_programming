#!/usr/bin/python3
def multiply_list_map(my_list:list=[], number=0):
    """
    multiply_list_map - a list with all values multiplied by a number
    @my_list: the list
    @number: the number
    Return: list with all values multiplied by a number
    """
    return list(map(lambda x: x * number, my_list))

