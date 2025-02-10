#!/usr/bin/python3
"""Ceci est une desc"""


class Student:
    """Ceci est une desc"""
    def __init__(self, first_name, last_name, age):
        """Ceci est une desc"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Ceci est une desc"""
        if isinstance(attrs, list):
            return {attr: getattr(self, attr)
                    for attr in attrs if hasattr(self, attr)}
        return self.__dict__

    def reload_from_json(self, json):
        """Ceci est une desc"""
        for key, value in json.items():
            setattr(self, key, value)
