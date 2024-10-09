#!/usr/bin/python3

"""
This Python code demonstrates the concept of inheritance
to define a derived classes 'VerboseList'.
"""

class VerboseList(list):

    def append(self, item):
        super.append()
        print(f"Added [{item}] to the list.")


    def extend(self, iterable):
        super().extend(items)
        print(f"Extended the list with [{len(items)}] items.")


    def remove(self, item):
        super().remove(item)
        print(f"Removed [{item}] from the list.")


    def pop(self):
        item = super().pop(index)
        print(f"Popped [{item}] from the list.")
        return item
