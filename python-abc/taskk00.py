#!/usr/bin/python3

"""
This Python code demonstrates the concept of abstract classes and inheritance
to define an animal hierarchy with a base class `Animal` and derived classes
`Dog` and `Cat`. The `Animal` class is an abstract class with an abstract method
`sound()` that derived classes must implement.
"""

from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def sound(self):
        """
        This method is abstract and must be implemented by derived classes.
        It defines the expected behavior of making an animal sound.
        """
        pass


class Dog(Animal):
    def __init__(self, name):
        self.name = name

    def sound(self):
        print("Woof! My name is", self.name)  # Enhanced output with dog's name


class Cat(Animal):
    def __init__(self, name):
        self.name = name

    def sound(self):
        print("Meow! My name is", self.name)  # Enhanced output with cat's name)


# Example usage
my_dog = Dog("Buddy")
my_cat = Cat("Whiskers")

my_dog.sound()  # Output: Woof! My name is Buddy
my_cat.sound()  # Output: Meow! My name is Whiskers