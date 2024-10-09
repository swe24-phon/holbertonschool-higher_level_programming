#!/usr/bin/python3

"""
This Python code demonstrates the concept of inheritance
to define a derived classes 'VerboseList'.
"""

class VerboseList(list):
    """
    Extend list in-built class
    """

    def append(self, item):
        super().append(item)
        print(f"Added [{item}] to the list.")


    def extend(self, iterable):
        super().extend(iterable)
        print(f"Extended the list with [{len(iterable)}] items.")


    def remove(self, item):
        super().remove(item)
        print(f"Removed [{item}] from the list.")


    def pop(self, index):
        item = super().pop(index)
        print(f"Popped [{item}] from the list.")
        return item
