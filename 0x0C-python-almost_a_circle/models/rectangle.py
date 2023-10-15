#!/usr/bin/python3
""" 1-rectangle  """
from models.base import Base


class Rectangle(Base):
    """This is the rectangle class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        self.integer_validator(width=width, height=height, x=x, y=y)
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    def getWidth(self):
        return self.__width

    def getHeight(self):
        return self.__height

    def getX(self):
        return self.__x

    def getY(self):
        return self.__y

    def setWidth(self, new_width):
        self.integer_validator(width=new_width)
        self.__width = new_width

    def setHeight(self, new_height):
        self.integer_validator(height=new_height)
        self.__height = new_height

    def setX(self, new_x):
        self.integer_validator(x=new_x)
        self.__x = new_x

    def setY(self, new_y):
        self.integer_validator(y=new_y)
        self.__y = new_y

    def integer_validator(self, **kwargs):
        for name, value in kwargs.items():
            if type(value) != int:
                raise TypeError("{} must be an integer".format(name))
            if value <= 0 and name in ["width", "height"]:
                raise ValueError("{} must be > 0".format(name))
            if value < 0 and name in ["x", "y"]:
                raise ValueError("{} must be >= 0".format(name))

    def area(self):
        return self.__width * self.__height

    def display(self):
        for i in range(self.__height):
            print(self.__width * "#")

    def __str__(self) -> str:
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id,
            self.__x,
            self.__y,
            self.__width,
            self.__height,
        )
