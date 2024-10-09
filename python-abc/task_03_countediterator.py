#!/usr/bin/python3

"""
This Python code demonstrates the concept of inheritance
to define a derived classes 'CountedIterator'.
"""


class CountedIterator:
    """
    A class that extends the functionality of an iterator
    to keep track of the number of items iterated.
    """

    def __init__(self, iterable):
        self.iterable = iter(iterable)
        self.count = 0

    def get_count(self):
        """
        Return the count of items iterated.
        """
        return self.count

    def __iter__(self):
        return self

    def __next__(self):
        next_item = next(self.iterable)
        self.count += 1
        return next_item
    