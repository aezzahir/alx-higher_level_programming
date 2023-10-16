#!/usr/bin/python3
""" Square  """
from models.rectangle import Rectangle


class Square(Rectangle):
    """This is the square class that inherit from rectangle class"""

    def __init__(self, size, x=0, y=0, id=None):
        self.size = size
        super().__init__(width=size, height=size, x=x, y=y, id=id)

    def __str__(self) -> str:
        return "[Square] ({}) {}/{} - {}".format(
            self.id,
            self._Rectangle__x,
            self._Rectangle__y,
            self._Rectangle__width,
        )

    @property
    def size(self):
        return self.getWidth()

    @size.setter
    def size(self, value):
        self.setWidth(value)
        self.setHeight(value)
