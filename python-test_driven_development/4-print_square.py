#!/usr/bin/python3
"""

This module is composed by a function that prints a square with the character #

"""


def print_square(size):
    """
    Print square with the character '#'.

    Parameters:
        size: integer size of the square

    Returns:
        None

    Raises:
        TypeError: if not integer
        ValueError: if size < 0
        TypeError: if float or < 0
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    for i in range(size):
        print("#" * size)
