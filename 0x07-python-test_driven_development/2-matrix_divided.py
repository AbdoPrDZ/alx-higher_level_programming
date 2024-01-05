#!/usr/bin/python3

"""
2-matrix_divided.py - divide matrix module
"""


def matrix_divided(matrix, div):
    """
    matrix_divided - divide all elements of a matrix by div argument

    Args:
        matrix (list): a list of lists of ints or floats
        div (int/float): the divisor number
    Raises:
        TypeError: matrix must be a matrix (list of lists) of integers/floats
        TypeError: Each row of the matrix must have the same size
        TypeError: div must be a number
        ZeroDivisionError: division by zero
    Returns:
        A new matrix with the result of the division
    """

    chckEl = lambda el: isinstance(el, int) or isinstance(el, float)
    chckRow = lambda row: isinstance(row, list) and all(list(map(chckEl, row)))

    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")
    elif div == 0:
        raise ZeroDivisionError("division by zero")
    elif (
        not isinstance(matrix, list)
        or len(matrix) == 0
        or not all(list(map(chckRow, matrix)))
    ):
        raise TypeError(
            "matrix must be a matrix (list of lists) \
of integers/floats"
        )
    elif not all(list(map(lambda row: len(row) == len(matrix[0]), matrix))):
        raise TypeError("Each row of the matrix must have the same size")

    return list(
        map(
            lambda row: list(map(lambda el: round(el / div, 2), row)),
            matrix,
        )
    )
