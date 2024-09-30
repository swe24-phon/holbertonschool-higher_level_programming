#!/usr/bin/python3
"""
This module contains a class Mylist that inherits from list
"""


class MyList(list):
    """
    This class inherits from list
    """
    def print_sorted(self):
        """
        This method prints the sorted list
        Parameters:
        self: the list of integers
        """

        print(sorted(self))
