#!/usr/bin/python3
"""
This module provides a method to check the type of an object.

The module contains the following method:
- is_kind_of_class(obj, a_class): Checks if an object is an instance of, or if the object is an instance of a class that inherited from, the specified class.
"""


def is_kind_of_class(obj, a_class):
    """Check if object is an instance of, or if the object is an instance of a class that inherited from, the specified class"""
    return isinstance(obj, a_class)
