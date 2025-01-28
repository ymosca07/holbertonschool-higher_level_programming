#!/usr/bin/python3
"""
    A class that defines a square.
"""


class Square:
    """
    A class that defines a square.
    """
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position 

    @property
    def size(self):
        """Getter = accéder valeurt attribut privé"""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter = modifier valeur attribut privé
        en s'assurant qu'elle est valide"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Retourne l'aire du carré"""
        return self.__size * self.__size
    
    @property
    def position(self):
        """Getter = accéder valeurt attribut privé"""
        return self.__position
    
    @position.setter
    def position(self, value):
        """Setter = modifier valeur attribut privé
        en s'assurant qu'elle est valide"""
        if not (
            isinstance(value, tuple)
            and len(value) == 2
            and all(isinstance(i, int) and i >= 0 for i in value)
        ):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        """Affiche le carré avec le caractère # en fonction de sa taille et position."""
        if self.__size == 0:
            print("")
            return

        [print("") for _ in range(self.__position[1])]

        for _ in range(self.__size):
            print(" " * self.__position[0], end="")
            print("#" * self.__size)
