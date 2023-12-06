#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    """
    simple_delete - delete item from directory
    @a_directory: the directory
    @key: argument will be always a string
    """
    if key in a_dictionary.keys():
        del a_dictionary[key]

    return a_dictionary
