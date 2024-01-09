#!/usr/bin/python3

"""
4-from_json_string - This module contains from_json_string function
"""

import json


def from_json_string(my_str):
    """
    from_json_string - convert json string to dict object

    Args:
        my_str (string): the json string

    Raises:
        JSONDecodeError: json decode error

    Returns:
        dict: the object dict
    """

    return json.loads(my_str)
