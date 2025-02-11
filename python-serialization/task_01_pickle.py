#!/usr/bin/env python3
"""Ceci est une description"""
import pickle


class CustomObject:
    """Ceci est une classe"""
    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student
    
    def display(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        with open(filename, "wb") as file:
            pickle.dump(self, file)
        return filename

    @classmethod 
    def deserialize(cls, filename):
        with open(filename, "rb") as file:
            cls = pickle.load(file)
        return cls
