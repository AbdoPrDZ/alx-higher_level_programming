#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    """
    update_dictionary - update directory value with specified key
    @a_directory: the directory
    @key: argument will be always a string
    @value: argument will be any type
    """
    a_dictionary[key] = value
    return a_dictionary
