#!/usr/bin/python3
"""Ceci est une description"""


class Student:
    """Ceci est une description"""
    def __init__(self, first_name, last_name, age):
        """Ceci est une description"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Ceci est une description"""
        return self.__dict__
    