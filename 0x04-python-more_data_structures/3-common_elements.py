#!/usr/bin/python3
def common_elements(set_1, set_2):
    """
    common_elements - get a set of common items in two sets
    @set_1: the first set
    @set_2: the second set
    Return: the set of common elements in two sets
    """
    com_set = set()
    for x in set_1:
        for y in set_2:
            if x == y and x not in com_set:
                com_set.add(x)

    return com_set
