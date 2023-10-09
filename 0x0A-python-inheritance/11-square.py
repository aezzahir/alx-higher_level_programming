#!/usr/bin/python3
"""This module contains a class Square that inherits from
Rectangle with specific string representation."""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A class representing squares with a specific string representation."""

    def __init__(self, size):
        """Initialize size."""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """Return a formatted string."""
        return "[Square] {}/{}".format(self.__size, self.__size)
