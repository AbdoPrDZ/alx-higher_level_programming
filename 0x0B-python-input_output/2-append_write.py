#!/usr/bin/python3

"""
2-append_write - This module contains append_write function
"""


def append_write(filename="", text=""):
    """
    append_write - create file if not exists and write in there

    Args:
        filename (str, optional): the file name. Defaults to "".
        text (str, optional): the file content text. Defaults to "".

    Returns:
        int: the written text length
    """

    with open(filename, "a", encoding="utf-8") as file:
        return file.write("{}".format(text))
