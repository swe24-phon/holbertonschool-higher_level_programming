#!/usr/bin/python3
def square_matrix_simple(matrix):
    """Returns a new matrix where each element is the square of the corresponding element in the input matrix
    parameters:
    matrix (list): A 2D list of integers
    Returns:
    list: A 2D list of integers
    """
    return [[element ** 2 for element in row] for row in matrix]