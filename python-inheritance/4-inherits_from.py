#!/usr/bin/python3
"""Ceci est une description"""


def inherits_from(obj, a_class):
    """Ceci est une description"""
    if type(obj) is not a_class and issubclass(type(obj), a_class) == 1:
        return True
    else:
        return False
