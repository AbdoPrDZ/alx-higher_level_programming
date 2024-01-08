#!/usr/bin/python3
"""
2-is_kind_of_class - This module defines is_kind_of_class function
"""


def is_kind_of_class(obj, a_class):
    """
    is_kind_of_class - check if object is instance
                       or inherited instance of a class

    Args:
        obj (any): the object
        a_class (type): the class

    Returns:
        bool: True if is instance or inherited, False if not
    """

    return isinstance(obj, a_class)
