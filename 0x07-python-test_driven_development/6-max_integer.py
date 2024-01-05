#!/usr/bin/python3
"""Module to find the max integer in a list
"""


def max_integer(list=[]):
    """
    max_integer - find the maximum on list

    Args:
        list (list, optional): the list. Defaults to [].

    Returns:
        int: the maximum
    """

    if len(list) == 0:
        return None

    _max = list[0]
    for el in list:
        if el > _max:
            _max = el

    return _max
