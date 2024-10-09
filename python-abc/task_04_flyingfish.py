#!/usr/bin/python3

"""
This Python code demonstrates the concept of inheritance
to define a derived classes 'CountedIterator'.
"""


class Fish:
    """
    A fish class.
    """

    def swim(self):
        """
        Return the method swim
        """
        return print("The fish is swimming")

    def habitat(self):
        """
        Return the method habitat
        """
        return print("The fish lives in water") 

class Bird:
    """
    A bird class
    """

    def fly(self):
        """
        Return the method fly
        """
        return print("The bird is flying") 

    def habitat(self):
        """
        Return the method habitat
        """
        return print("The bird lives in the sky")

class FlyingFish(Fish, Bird):
    """
    A class that extends the functionality of an iterator
    to keep track of the number of items iterated.
    """

    def fly(self):
        """
        Return the method fly, override parent
        """
        return print("The flying fish is soaring!") 

    def swim(self):
        """
        Return the method swim, override parent
        """
        return print("The flying fish is swimming!")

    def habitat(self):
        """
        Return the method habitat, override parent
        """
        return print("The flying fish lives both in water and the sky!")
