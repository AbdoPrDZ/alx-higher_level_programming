#!/usr/bin/python3
"""
0-lookup - This module defines lookup function
"""


def lookup(obj):
    """
    lookup - get object attributes and methods list

    Args:
        obj (Object): the object

    Returns:
        list: list of attributes and methods
    """

    return dir(obj)
