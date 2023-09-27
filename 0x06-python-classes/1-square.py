#!/usr/bin/python3
"""
This module defines a class called Square and provides documentation for it.

The Square class represents a square shape with a given size.

Classes:
    Square: A class to create and manipulate square objects.

"""


class Square:
    """
    A class to create and manipulate square objects.
    Attributes:
        __size (int): The size of the square side.
    Methods:
        __init__(self, size):
            Initializes a new Square instance.
    """
    def __init__(self, size):
        """
        Initializes a new Square instance.
        Args:
            size (int): The size of the square's side.
        """
        self.__size = size
