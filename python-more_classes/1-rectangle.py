#!/usr/bin/python3

"""
This module provides a function that
create a Rectangle class
"""


class Rectangle:
    """
    create empty Rectangle class

    """
    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height

    @property
    def width(self):
        return self.__width
    @width.setter
    def width(self, value):
        self.__width = value
    @property
    def height(self):
        return self.__height
    @height.setter
    def height(self, value):
        self.__height = value
