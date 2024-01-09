#!/usr/bin/python3

"""
7-add_item.py - add argv items to add_item.json file
"""

import sys

save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file

if __name__ == "__main__":
    JSON_FILENAME = "add_item.json"

    try:
        _list = load_from_json_file(JSON_FILENAME)
    except Exception as e:
        _list = []

    for item in sys.argv[1:]:
        _list.append(item)

    save_to_json_file(_list, JSON_FILENAME)
