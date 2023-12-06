#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    """
    only_diff_elements - get a set of all elements present in only one set
    @set_1: the first set
    @set_2: the second set
    Return: a set of all elements present in only one set
    """
    diff_set = set()
    for x in set_1:
        if x not in set_2 and x not in diff_set:
            diff_set.add(x)
    for y in set_2:
        if y not in set_1 and y not in diff_set:
            diff_set.add(y)
    return diff_set
