#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    """Prints a matrix of integers.
    Parameter:
    matrix (list): A 2D list of integers.
    """
    for row in matrix:
        for num in row:
            print("{:d}".format(num), end=" ")
        print()
    if not matrix:
        print()
