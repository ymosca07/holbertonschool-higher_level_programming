#!/usr/bin/python3
"""
    A class that defines a square.
"""


class Square:
    """
    A class that defines a square.
    """
    def __init__(self, size=0):
        self.__size = size
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        return self.__size * self.__size
