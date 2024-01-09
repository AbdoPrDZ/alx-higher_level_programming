#!/usr/bin/python3

"""
0-read_file - This module contains read_file function
"""


def read_file(filename=""):
    """
    read_file - read file content and print it

    Args:
        filename (str, optional): the file name. Defaults to "".
    """
    with open(filename, "r", encoding="utf-8") as file:
        print(file.read(), end="")
