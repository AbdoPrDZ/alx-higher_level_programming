#!/usr/bin/python3
def inherits_from(obj, a_class):
    """
    inherits_from - checks if object is inherited instance of a class

    Args:
        obj (any): the object
        a_class (type): the type

    Returns:
        bool: True if object is inherited instance of a class, if not
    """

    return issubclass(type(obj), a_class) and type(obj) is not a_class
