#!/usr/bin/python3
class Square:
    """Square with size validation, area computation, and printing capabilities"""

    def __init__(self, size=0):
        """Initialize a new square."""
        self.size = size

    @property
    def size(self):
        """Get the current size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the current square area."""
        return self.__size * self.__size

    def my_print(self):
        """Print the square with # character."""
        if self.__size == 0:
            print()
            return
        for i in range(self.__size):
            print("#" * self.__size)
