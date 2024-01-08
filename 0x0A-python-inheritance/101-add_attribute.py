#!/usr/bin/python3
"""
101-add_attribute.py - This module defines a add_attribute function
"""


def add_attribute(object, attr_name, value):
    """
    add_attribute - add a new attribute to object if can

    Args:
        object (any): the object
        attr_name (str): the attribute name
        value (any): the attribute value

    Raises:
        TypeError: can't add new attribute
    """

    if not hasattr(object, "__dict__"):
        raise TypeError("can't add new attribute")

    setattr(object, attr_name, value)
