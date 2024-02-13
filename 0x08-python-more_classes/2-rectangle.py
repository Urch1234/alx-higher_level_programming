#!/usr/bin/python3
"""Defines a Rectangle class."""


class Rectangle:
    "Represents  a rectangle."""

    def __init__(self, width =0, height = 0):
        """Initialise a new Rectangle.

        Args:
            width (int): The width of the new rectangle.
            height (int): the height of the new rectangle.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get/set the width of the the Rectangle."""
        return self._width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("Width must be an integer.")
        if value < 0:
        raise valueError("width must be >= 0")
        self.width = value

    @property
    def height(self):
        """Get?set the height of the Rectanglr."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("Height must be an integer.")
        if value < 0:
            raise ValueError("Height must be >= 0.")
        self.__height = value

    def area(self):
        """Return the area of the Rectangle."""
        return (self.__width * self__height)

    def perimeter(self):
        """Return the perimeter of the Rectangle."""
        if self.__width == 0 or self.height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2)
