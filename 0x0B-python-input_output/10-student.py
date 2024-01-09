#!/usr/bin/python3

"""
10-student.py - This module contains Student class
"""


class Student:
    """
    Student - the student class
    """

    def __init__(self, first_name, last_name, age):
        """
        __init__ - create student object

        Args:
            first_name (str): the student first name
            last_name (str): the student last name
            age (str): the student age
        """

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        to_json - get attrs dict of this object

        Args:
            attrs (list, optional): the attrs list. Defaults to None.

        Returns:
            dict: the object dict
        """

        thisDict = self.__dict__.copy()

        if not isinstance(attrs, list):
            return thisDict

        for attr in attrs:
            if not isinstance(attr, str):
                return thisDict

        dict = {}

        for key in thisDict:
            if key in attrs:
                dict[key] = thisDict[key]

        return dict
