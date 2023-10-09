#!/usr/bin/python3
"""This module contains a class Square that inherits
from Rectangle."""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A class representing squares."""

    def __init__(self, size):
        """Initialize size."""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """Return the area of the square."""
        return self.__size * self.__size
