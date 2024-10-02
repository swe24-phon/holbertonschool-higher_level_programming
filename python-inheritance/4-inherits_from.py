#!/usr/bin/python3
"""
This module provides a method to check if an object is an instance
 of a class that inherited from a specified class.

The module contains the following method:
- inherits_from(obj, a_class): Checks if an object is an instance of
 a class that inherited from the specified class.
"""

def inherits_from(obj, a_class):
    """Check if object is an instance of a class that inherited
    from the specified class"""
    return issubclass(type(obj), a_class)
