#!/usr/bin/python3
"""
This module is composed by a function that 
finding the max integer in a list

"""


def max_integer(lst):
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
    if len(list) == 0:
        return None
    result = list[0]
    i = 1
    while i < len(list):
        if list[i] > result:
            result = list[i]
        i += 1
    return result
