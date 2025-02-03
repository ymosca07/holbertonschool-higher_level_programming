#!/usr/bin/python3
"""Ceci est une description"""


class MyList(list):
    """Ceci est une description"""
    def print_sorted(self):
        if isinstance(self, int) == 1:
            raise TypeError("Ceci doit être un entier...")
        else:
            print(sorted(self))
