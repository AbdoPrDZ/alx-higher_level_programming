#!/usr/bin/python3

"""
0-add_integer.py - integer addition module
"""


def add_integer(a, b=98):
    """add_integer - calculate the addition of a and b

    Args:
        a (int, float): the first number
        b (int, float): the second number. Defaults to 98

    Raises:
        TypeError: a must be an integer
        TypeError: b must be an integer

    Returns:
        int: the addition of a and b
    """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    elif not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")

    a = int(a)
    b = int(b)

    return a + b
