#!/usr/bin/python3
"""Ceci est une description"""


class MyList(list):
    """Ceci est une description"""
    def print_sorted(self):
        if isinstance(list, int) == 1:
            raise TypeError("Uniquement les entiers sont acceptés...")
        else:
            print(sorted(self))
