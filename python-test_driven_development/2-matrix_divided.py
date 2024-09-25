#!/usr/bin/python3

"""
This module provides a function that divides all elements of a matrix.
"""


def matrix_divided(matrix=None, div=None):
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

    if matrix is None and div is None:
        raise TypeError("matrix_divided() missing 2 required positional "
                        "arguments: 'matrix' and 'div'")
    if matrix is None:
        raise TypeError("matrix_divided() missing 1 required positional "
                        "argument: 'matrix'")
    if div is None:
        raise TypeError("matrix_divided() missing 1 required positional "
                        "argument: 'div'")

    if (not isinstance(matrix, list) or not matrix or
            not all(isinstance(row, list) for row in matrix)):
        raise TypeError("matrix must be a matrix (list of lists) of "
                        "integers/floats")

    if not all(isinstance(elem, (int, float))
               for row in matrix for elem in row):
        raise TypeError("matrix must be a matrix (list of lists) of "
                        "integers/floats")

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[0.0 if div == float('inf') else round(elem / div, 2)
             for elem in row] for row in matrix]