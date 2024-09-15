#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    """Prints a matrix of integers.
    Parameter:
    matrix (list): A 2D list of integers.
    """
    for row in matrix:
        print(" ".join("{:d}".format(num) for num in row))
    if not matrix:
        print()
