#!/usr/bin/python3
"""
This module contains the Rectangle class.
"""
from models.base import Base


class Rectangle(Base):
    """
    Defines a Rectangle class that inherits from Base.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize a new Rectangle."""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def _validate_int(self, name, value):
        """Validate and set an integer value."""
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if name in ["width", "height"] and value <= 0:
            raise ValueError("{} must be > 0".format(name))
        elif name in ["x", "y"] and value < 0:
            raise ValueError("{} must be >= 0".format(name))
        return value

    @property
    def width(self):
        """Get or set the width of the Rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        self.__width = self._validate_int("width", value)

    @property
    def height(self):
        """Get or set the height of the Rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        self.__height = self._validate_int("height", value)

    @property
    def x(self):
        """Get or set the x coordinate of the Rectangle."""
        return self.__x

    @x.setter
    def x(self, value):
        self.__x = self._validate_int("x", value)

    @property
    def y(self):
        """Get or set the y coordinate of the Rectangle."""
        return self.__y

    @y.setter
    def y(self, value):
        self.__y = self._validate_int("y", value)

    def area(self):
        """Return the area of the Rectangle."""
        return self.width * self.height

    def display(self):
        """Display the Rectangle."""
        for i in range(self.__y):
            print()
        for i in range(self.__height):
            print(self.__x * " " + self.__width * "#")

    def __str__(self) -> str:
        """Display the Rectangle's informations."""
        return "[Square] ({}) {}/{} - {}".format(
            self.id,
            self._Rectangle__x,
            self._Rectangle__y,
            self._Rectangle__width,
        )

    def update(self, *args, **kwargs):
        """Update the Rectangle's attributes."""
        if not args and args is not []:
            for name, value in kwargs.items():
                if name == "id":
                    self.id = value
                if name == "x":
                    self.setX(value)
                if name == "y":
                    self.setY(value)
                if name == "width":
                    self.setWidth(value)
                if name == "height":
                    self.setHeight(value)

        try:
            self.id = args[0]
            self.__width = args[1]
            self.__height = args[2]
            self.__x = args[3]
            self.__y = args[4]
        except IndexError:
            pass

    def to_dictionary(self):
        """Return a dictionary representation of the Rectangle."""
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y,
        }
