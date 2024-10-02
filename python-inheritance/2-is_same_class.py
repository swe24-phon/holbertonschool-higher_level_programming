#!/usr/bin/python3
"""
This module def is_same_class compare class to instance
of class
"""


def is_same_class(obj, a_class):
    """Check if object is exactly an instance of the specified class"""
    return type(obj) is a_class
