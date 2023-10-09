#!/usr/bin/python3
"""This module contains a class MyInt that inherits from
int and inverts == and !=."""


class MyInt(int):
    """A class that represents MyInt which has inverted == and != operators."""

    def __eq__(self, other):
        """Invert the == operator."""
        return super().__ne__(other)

    def __ne__(self, other):
        """Invert the != operator."""
        return super().__eq__(other)
