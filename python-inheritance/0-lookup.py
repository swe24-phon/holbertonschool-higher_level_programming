#!/usr/bin/python3
"""
This module use dir to provides a function that returns
the list of available all attributes and methods in an object
"""


def lookup(obj):
    """
    Prints all available attributes and methods that the object can ultilise

    Parameters:
    obj: a class passed in as parameter

    Returns:
    a list object

    """
    return dir(obj)
