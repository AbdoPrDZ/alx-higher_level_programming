#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    """
    print_matrix_integer - Print a matrix of integers
    @matrix: The matrix want to print
    """
    for row in matrix:
        rLen = len(row)
        for i in range(rLen):
            print('{}'.format(row[i]), end='')
            if i < rLen - 1:
                print(' ', end='')
        print('$')
