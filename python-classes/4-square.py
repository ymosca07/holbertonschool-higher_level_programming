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

    @property
    def size(self):
        """Getter = accéder valeurt attribut privé"""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter = modifier valeur attribut privé en s'assurant
        qu'elle est valide"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Retourne l'aire du carré"""
        return self.__size * self.__size
