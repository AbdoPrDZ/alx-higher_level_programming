#!/usr/bin/python3
class MagicClass:
    """
    MagicClass - Class to store properties of circumference
    """

    def __init__(self, radius=0):
        """"
        __init__ - Init the magic class with radius

        Args:
            radius (int): the circumference radius. Default to 0.
        """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):

        """
        area - Calculates the area of the circumference

        Return:
            float : The area of the circumference
        """
        import math

        return ((self.__radius ** 2) * math.pi)

    def circumference(self):
        """
        circumference - Calculates the perimeter of a circumference

        Returns:
            float: The perimeter of a circumference
        """
        import math

        return (2 * math.pi * self.__radius)
