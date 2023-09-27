#!/usr/bin/python3
"""
This is the "2-square" module.
It supplies one class, Square.
"""


class Square:
    """A Square class with a size attribute and validations"""

    def __init__(self, size=0):
        """Initialize a new Square instance with a given size
        Args:
            size (int): Size of the side of the square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
