#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    """
    divisible_by_2 - Find all multiples of 2 in a list
    @my_list: The list want to search inside
    Return: Result list
    """
    return [item % 2 == 0 for item in my_list]
