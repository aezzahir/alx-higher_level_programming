#!/usr/bin/python3
"""This module contains a class BaseGeometry with an integer validator."""


class BaseGeometry:
    """A class with methods 'area' and 'integer_validator'."""

    def area(self):
        """Not yet implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate 'value' as integer."""
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
