#!/usr/bin/python3

"""
6-load_from_json_file - This module contains from_json_string function
"""

import json


def load_from_json_file(filename):
    """
    from_json_string - convert json file content to dict object

    Args:
        filename (string): the json filename

    Raises:
        JSONDecodeError: json decode error

    Returns:
        dict: the object dict
    """

    with open(filename, "r", encoding="utf-8") as file:
        return json.loads(file.read())
