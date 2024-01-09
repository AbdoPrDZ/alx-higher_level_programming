#!/usr/bin/python3

"""
5-save_to_json_file - This module contains save_to_json_file function
"""

import json


def save_to_json_file(my_obj, filename):
    """
    save_to_json_file - create json file for our object

    Args:
        my_obj (dict): the object dict
        filename (str): the json file name

    Returns:
        int: the written text length
    """

    with open(filename, "w") as file:
        return file.write(json.dumps(my_obj))
