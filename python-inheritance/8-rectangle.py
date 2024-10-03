#!/usr/bin/python3
"""
This module provides class BaseGeometry.
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """class Rectangle
    
        """
    def __init__(self, width, height):
        """Method to initialize the class Rectangle"""
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height
