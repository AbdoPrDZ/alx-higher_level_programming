#!/usr/bin/python3

"""
8-class_to_json.py - This module contains class_to_json function
"""


def class_to_json(obj):
    """
    class_to_json - get object dict

    Args:
        obj (object): the object

    Returns:
        _type_: the object dict
    """

    return obj.__dict__.copy() if hasattr(obj, "__dict__") else {}
