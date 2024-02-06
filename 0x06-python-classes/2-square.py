#!/usr/bin/python3


class Square:

    def __init__(self, size=0):
        """Initialise a new Square.
        
        Args:
            size (int): Thee size of the new sauare.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise valueError("size must be >= 0")

        self.__size = size
