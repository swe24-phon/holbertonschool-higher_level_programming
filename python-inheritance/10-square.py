#!/usr/bin/python3
"""
This module provides class BaseGeometry.
"""

Rectangle = __import__('9-rectangle.py').Rectangle


class Square(Rectangle):
    """class Square
    """

    def __init__(self, size):
        """Method to initialize the class Square"""
        super().integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
