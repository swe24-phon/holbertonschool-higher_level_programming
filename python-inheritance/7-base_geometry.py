#!/usr/bin/python3
"""
This module provides class BaseGeometry.
"""


class BaseGeometry:
    """class BaseGeometry

    """
    def area(self):
        """Method raises an Exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates a value.
        If value is not integer, raise a TypeError
        If value <= 0, raise a Value error
        """
        if not isinstance(value, int) or isinstance(value, bool):
            raise TypeError(name + " must be an integer")
        if value <= 0:
            raise ValueError(name + " must be greater than 0")
