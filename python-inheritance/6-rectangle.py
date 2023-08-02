#!/usr/bin/python3
"""Defines a class Rectangle that inherits from BaseGeometry."""

class BaseGeometry:
    def area(self):
        raise Exception("area() is not implemented")



class Rectangle(BaseGeometry):
    def __init__(self, width, height):
        """Intialize a new Rectangle.
        
        Args:
            width (int): The width of the new Rectangle.
            height (int): The height of the new Rectangle.
        """
        self.__width = width
        self.__height = height
        self.integer_validator("width", self.__width)
        self.integer_validator("height", self.__height)
