#!/usr/bin/python3
"""
This module is composed by a function that 
finding the max integer in a list

"""


def max_integer():
    """
    Returns the maximum integer in the input list.

    PARAMETERS:
        lst (list, optional): The input list of integers. Defaults to an empty list.

    Returns:
        int: The maximum integer in the input list.

    Raises:
        ValueError: If the input list is empty.
        TypeError: If the input list contains non-integer elements.
    """
    if not lst:
        raise ValueError("Input list is empty")

    for element in lst:
        if not isinstance(element, int):
            raise TypeError("Input list contains non-integer elements")

    return max(lst)
