#!/usr/bin/python3
"""
4-print_square.py - print a squire module
"""


def print_square(size):
    """
    print_square - print a square with the # character

    Args:
        size (int): the height/width of the square
    Raises:
        TypeError: size must be an integer
        ValueError: size must be >= 0
    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")

    print((("#" * size) + "\n") * size, end="")
