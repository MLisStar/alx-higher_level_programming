#!/usr/bin/python3
# 1-rectangle.py

""Defines rectangle class.""

class Rectanglee:
    "Represent rectangle"

    def __init__(self, width=0, height=0):
        ""initialize new rect.

        Args:
            width (int): The width of the new rect.
            height (int): height of new rect.
        ""

    self.width = width
    self.height = height

    @property
    def width(self):
        """Get/set the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get/set the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
            