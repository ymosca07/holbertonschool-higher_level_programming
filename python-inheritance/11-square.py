#!/usr/bin/python3
"""Ceci est une description"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Ceci est une description"""

    def __init__(self, size):
        """Initialise un carré avec `size`, validé par integer_validator."""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Retourne l'aire du carré."""
        return self.__size * self.__size

    def __str__(self):
        """Retourne la description du carré sous la forme [Square] <size>/<size>."""
        return f"[Square] {self.__size}/{self.__size}"
