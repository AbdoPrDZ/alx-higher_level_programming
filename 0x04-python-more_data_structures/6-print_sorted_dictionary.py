#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    """
    print_sorted_dictionary - print directory in sort way
    @a_directory: the directory
    """
    if a_dictionary:
        keys = list(a_dictionary.keys())
        keys.sort()

        for key in keys:
            print('{0}: {1}'.format(key, a_dictionary[key]))
