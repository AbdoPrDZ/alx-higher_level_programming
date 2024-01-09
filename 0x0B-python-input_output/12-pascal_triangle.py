#!/usr/bin/python3

"""
12-pascal_triangle - This module contains pascal_triangle function
"""


def pascal_triangle(n):
    """
    pascal_triangle - create pascal triangle

    Args:
        n (int): the triangle size

    Returns:
        list: the triangle
    """

    if n <= 0:
        return []

    triangle = []

    for i in range(1, n + 1):
        row = []

        for j in range(1, i + 1):
            row.append(j if j < (i + 1) / 2 else i + 1 - j)

        triangle.append(row)

    return triangle
