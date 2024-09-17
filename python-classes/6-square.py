#!/usr/bin/python3
"""
This is the "Square"  module.
This module provides a simple Square class.
with initialize size.
Size defaults to 0. Raise errors on invalid inputs.
Methods Getter and Setter properties for size.
Method area returns size of area of the square.
Method my_print prints the square using "#".
"""


class Square:
    """
    define class for Square
    """
    def __init__(self, size=0):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        return self.__size ** 2

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        if self.__size == 0:
            print("")
        for i in range(self.__size):
            for j in range(self.__size):
                print("#", end="")
            print()
