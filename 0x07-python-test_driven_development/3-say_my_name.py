#!/usr/bin/python3
"""
3-say_my_name.py - print name module
"""


def say_my_name(first_name, last_name=""):
    """
    say_my_name - print the name

    Args:
        first_name (str): first_name must be a string
        last_name (str): last_name must be a string
    Raises:
        TypeError: If either of first_name or last_name are not strings
    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    elif not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {0} {1}".format(first_name, last_name))
