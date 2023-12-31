#!/usr/bin/python3
"""
2-is_same_class.py - Module defines is_same_class function
"""


def is_same_class(obj, a_class):
    """
    is_same_class - check if `obj` is the same of `class a_class`

    Args:
        obj (any): the object
        a_class (type): the class

    Returns:
        bool: True if is the same, False if not
    """

    return type(obj) is a_class
