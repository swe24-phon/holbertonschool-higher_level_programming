#!/usr/bin/python3
"""
This module contains a class Mylist that inherits from list
"""


class Mylist(list):
    """
    This class inherits from list
    Parameters:
    self: the list of integers    
    """
    def print_sorted(self):
        """This method prints the sorted list"""
        print(sorted(self))
