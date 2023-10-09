#!/usr/bin/python3
"""This module contains a class Rectangle that inherits
from BaseGeometry."""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """A class representing rectangles with area method and string
    representation."""

    def __init__(self, width, height):
        """Initialize width and height."""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Return the area of the rectangle."""
        return self.__width * self.__height

    def __str__(self):
        """Return a formatted string."""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
