#!/usr/bin/python3

"""
This Python code demonstrates the concept of inheritance
to define a derived classes 'VerboseList'.
"""


import math
from abc import ABC, abstractmethod
"""

"""

class VerboseList(list):
    @abstractmethod
    def append(self, item):
        super.append()
        print(f"Added [{item}] to the list.")

    @abstractmethod
    def extend(self, iterable):
        super().extend(items)
        print(f"Extended the list with [{len(items)}] items.")

    @abstractmethod
    def remove(self, item):
        super().remove(item)
        print(f"Removed [{item}] from the list.")

    @abstractmethod
    def pop(self):
        item = super().pop(index)
        print(f"Popped [{item}] from the list.")
        return item
