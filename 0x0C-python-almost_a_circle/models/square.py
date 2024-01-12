#!/usr/bin/python3
"""
square.py - This module defined a Square class inherits from Rectangle class
"""

from models.rectangle import Rectangle


class Square(Rectangle):

    """
    Square - the square class inherits from Rectangle class
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        __init__ - create the square instance

        Args:
            size (int): the square size
            x (int, optional): the square pos in x axis. Defaults to 0.
            y (int, optional): the square pos in y axis. Defaults to 0.
            id (int, optional): the square id. Defaults to None.
        """

        super().__init__(size, size, x, y, id)

    def update(self, *args, **kwargs):
        """
        update - update the instance attributes

        Args:
            args (list): the no-keyword arguments of new values
            kwargs (dict): the key-worded arguments of new values
        """

        args_len = len(args)

        if args_len != 0:
            self.id = args[0] if args_len >= 1 else self.id
            self.size = args[1] if args_len >= 2 else self.size
            self.x = args[2] if args_len >= 3 else self.x
            self.y = args[3] if args_len >= 4 else self.y
        else:
            self.id = kwargs["id"] if "id" in kwargs.keys() else self.id
            self.size = kwargs["size"] if "size" in kwargs.keys() else self.size
            self.x = kwargs["x"] if "x" in kwargs.keys() else self.x
            self.y = kwargs["y"] if "y" in kwargs.keys() else self.y

    def to_dictionary(self):
        """
        to_dictionary - convert current square instance to dict

        Returns:
            dict: the square dict
        """

        return {
            "id": self.id,
            "size": self.size,
            "x": self.x,
            "y": self.y,
        }

    @property
    def size(self):
        """
        size.getter - get the rectangle size

        Returns:
            int: the rectangle size
        """

        return self.width

    @size.setter
    def size(self, value):
        """
        size.setter - set the rectangle size

        Args:
            value (int): the rectangle size
        """

        self.width = value
        self.height = value

    def __str__(self):
        """
        __str__ - get the square string

        Returns:
            str: the square string
        """

        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}"
