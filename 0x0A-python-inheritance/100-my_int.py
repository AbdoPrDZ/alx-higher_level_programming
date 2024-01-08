#!/usr/bin/python3

"""
100-my_int.py - This module defines a MyInt class inherits from int
"""


class MyInt(int):

    """
    MyInt - MyInt a custom int class
    """

    def __eq__(self, obj):
        """
        __eq__ - get reverse of equal operation

        Args:
            obj (any): the other object

        Returns:
            bool: False if is equals, True if not
        """

        i = self * 1

        return i != obj

    def __ne__(self, obj):
        """
        __eq__ - get reverse of not equal operation

        Args:
            obj (any): the other object

        Returns:
            bool: True if not equals, False if is equals
        """

        i = self * 1

        return i == obj
