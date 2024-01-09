#!/usr/bin/python3

"""
1-write_file - This module contains write_file function
"""


def write_file(filename="", text=""):
    """
    write_file - create file if not exists and write in there

    Args:
        filename (str, optional): the file name. Defaults to "".
        text (str, optional): the file content text. Defaults to "".

    Returns:
        int: the written text length
    """

    with open(filename, "w") as file:
        return file.write("{}".format(text))
