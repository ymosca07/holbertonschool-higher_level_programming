#!/usr/bin/python3

class Square:

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
        if not isinstance(value, int):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):

        c = 0

        if self.__size == 0:
            print("")
        else:
            while c < self.__size:
                i = 0
                while i < self.__size:
                    print("#", end="")
                    i += 1
                print("")
                c += 1
