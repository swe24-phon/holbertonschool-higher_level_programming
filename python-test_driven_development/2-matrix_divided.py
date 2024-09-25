#!/usr/bin/python3

"""
This module provides a function that divides all elements of a matrix.
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a given divisor.

    Parameters:
        matrix (list of list of int/float): A list of lists where each inner
        list represents a row of the matrix.
        div (int/float): The divisor by which each element of the matrix will
          be divided.

    Returns:
        list of list of float: A new matrix with each element divided by the
          divisor.

    Raises:
        TypeError: If the matrix is not a list of lists of integers/floats,
          or if div is not an integer/float.
        TypeError: If the rows of the matrix are not of the same size.
        ZeroDivisionError: If div is zero.

    """

    if not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of"
                        " integers/floats")

    row_size = len(matrix[0])
    if not all(len(row) == row_size for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = [[round(float(elem) / div, 2) for elem in row]\
                   for row in matrix]

    return new_matrix
