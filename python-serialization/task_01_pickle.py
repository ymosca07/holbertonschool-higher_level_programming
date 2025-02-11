#!/usr/bin/env python3
"""Ceci est une description"""
import pickle


class CustomObject:
    """Ceci est une classe"""
    def __init__(self, name, age, is_student):
        """Ceci est une description"""
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Ceci est une description"""
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """Ceci est une description"""
        try:
            with open(filename, "wb") as file:
                pickle.dump(self, file)
            return filename
        except:
            return None

    @classmethod
    def deserialize(cls, filename):
        """Ceci est une description"""
        try:
            with open(filename, "rb") as file:
                data = pickle.load(file)
            return data
        except:
            return None
