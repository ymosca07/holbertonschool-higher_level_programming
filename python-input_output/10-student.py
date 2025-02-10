#!/usr/bin/python3
"""Ceci est une description"""


class Student:
    """Ceci est une description"""
    def __init__(self, first_name, last_name, age):
        """Ceci est une description"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Ceci est une description"""
        if attrs is type(list):
            return self.first_name and self.last_name
        else:
            return self.__dict__
