#!/usr/bin/python3
"""
base.py - This module defined a Base class for model class
"""


import json
import os


class Base:

    """
    Base - The base class for model class

    Attributes:
        __nb_objects (int): the number of base instances. Defaults to 0
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        __init__ - create base instance of our models

        Args:
            id (int, optional): the instance id. Defaults to None.
        """

        if not (id is None):
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        to_json_string - convert list of dict to json string

        Args:
            list_dictionaries (list): the list of dict

        Returns:
            str: the json string
        """

        if not (list_dictionaries is None or len(list_dictionaries) == 0):
            return json.dumps(list_dictionaries)
        else:
            return "[]"

    @classmethod
    def save_to_file(cls, list_objs):
        """
        save_to_file - save the list of base objects to file

        Args:
            list_objs (list(Base)): the list of base objects
        """

        filename = "{0}.json".format(cls.__name__)
        with open(filename, "w") as file:
            if list_objs is None or len(list_objs) == 0:
                file.write("[]")
            else:
                file.write(
                    Base.to_json_string(
                        [object.to_dictionary() for object in list_objs]
                    )
                )

    @staticmethod
    def from_json_string(json_string):
        """
        from_json_string - convert json string to list of dict

        Args:
            json_string (str): the json string

        Returns:
            list: the list of dict
        """

        if json_string is None or json_string == "[]":
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        create - create a base instance from dict

        Returns:
            Base: the base instance
        """

        if not (dictionary is None) and len(dictionary) != 0:
            if cls.__name__ == "Rectangle":
                new = cls(1, 1)
            else:
                new = cls(1)

            new.update(**dictionary)

            return new

    @classmethod
    def load_from_file(cls):
        """
        load_from_file - load list of Base object from json file

        Returns:
            list: the list of Base object
        """

        _list = []
        filename = "{}.json".format(cls.__name__)

        if os.path.exists(filename):
            with open(filename, "r") as file:
                items = Base.from_json_string(file.read())
                _list = [cls.create(**item) for item in items]

        return _list
