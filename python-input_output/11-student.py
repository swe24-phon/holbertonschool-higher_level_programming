#!/usr/bin/python3
"""
Write a class Student that defines a student
make it serialisable
"""


class Student:
    """ class Student """

    def __init__(self, first_name, last_name, age):
        """ init """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ return dictionary description with simple data structure """
        if attrs is not None:
            return {k: v for k, v in self.__dict__.items() if k in attrs}
        return self.__dict__
    
    def reload_from_json(self, json):
        """ reload from json """
        for k, v in json.items():
            setattr(self, k, v)
