#!/usr/bin/python3

"""
This Python code demonstrates the concept of abstract classes and inheritance
to define an animal hierarchy with a base class `Animal` and derived classes
`Dog` and `Cat`. The `Animal` class is an abstract class with an abstract
 method `sound()` that derived classes must implement.
"""

from abc import ABC, abstractmethod


class Animal(ABC):
    """
    sound method is abstract and must be implemented by derived classes.
    It defines the expected behavior of making an animal sound.
    """
    def __init__(self):
        pass

    @abstractmethod
    def sound(self):
        pass


class Dog(Animal):
    """
    class Dog extended from animal class
    must include sound
    """
    def __init__(self, name):
        self.name = name

    def sound(self):
        return "Bark"


class Cat(Animal):
    """
    class cat extended from animal class
    must include sound
    """
    def __init__(self, name):
        self.name = name

    def sound(self):
        return "Bark"
