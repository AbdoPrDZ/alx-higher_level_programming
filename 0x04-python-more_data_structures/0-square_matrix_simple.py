#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    """
    square_matrix_simple - calculate square of matrix
    @matrix: the matrix
    Return: the square of matrix
    """
    nMatrix = []
    i = 0
    for row in matrix:
        j = 0
        nMatrix.append([])
        for col in row:
            nMatrix[i].append(col * col)
            j += 1
        i += 1
    return nMatrix
