#!/usr/bin/python3

"""
3-to_json_string - This module contains to_json_string function
"""

import json


def to_json_string(my_obj):
    """
    to_json_string - convert object to json string

    Args:
        my_obj (dict): the dict object

    Raises:
        TypeError: Object of type set is not JSON serializable

    Returns:
        str: the json string
    """

    return json.dumps(my_obj)
