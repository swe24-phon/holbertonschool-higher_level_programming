#!/usr/bin/python3
"""
This module provides class BaseGeometry.
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """class Square
    """

    def __init__(self, size):
        """Method to initialize the class Square"""
        super().integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """Method to calculate the area of the square"""
        return self.__size ** 2

    def __str__(self):
        """Method to return a string representation of the square"""
        return "[Square] {}/{}".format(self.__size, self.__size)
