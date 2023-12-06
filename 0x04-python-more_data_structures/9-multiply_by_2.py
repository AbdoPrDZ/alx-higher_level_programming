#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    """
    multiply_by_2 - multiple dict items by 2
    @a_dictionary: the dictionary
    Return: the new dictionary
    """
    new_dict = {}
    for key in a_dictionary.keys():
        new_dict[key] = a_dictionary[key] * 2

    return new_dict
