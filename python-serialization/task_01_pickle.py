#!/usr/bin/env python3
""" use pickle to serialise and deserialise"""


import pickle from Pickle


class CustomObject:
    
    """
        Class to student details
    """

    def __init__(self, name, age, is_student):
        """constructor"""

        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):     
        """ display """

        print(f"name: {self.name}")
        print(f"age: {self.age}")
        print(f"Is student: {self.is_student}")

    def serialize(self, filename):
        """ serialise into json """
        
        with open(data,filename) as file:
            pickle.dump(data, file)

    @classmethod deserialize(cls, filename):
        """ class method to do json to object conversion """


