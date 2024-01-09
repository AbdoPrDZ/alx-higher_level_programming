#!/usr/bin/python3

"""
9-student.py - This module contains Student class
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

    def to_json(self):
        """
        to_json - get dict of this object

        Returns:
            dict: the object dict
        """

        return self.__dict__.copy()
