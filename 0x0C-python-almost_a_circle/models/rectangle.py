#!/usr/bin/python3
""" 1-rectangle  """
from models.base import Base


class Rectangle(Base):
    """This is the rectangle class"""

    def __init__(self, width, height, x=0, y=0, id=None):
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
        self.__width = new_width

    def setHeight(self, new_height):
        self.__height = new_height

    def setX(self, new_x):
        self.__x = new_x

    def setY(self, new_y):
        self.__y = new_y
