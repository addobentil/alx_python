#!/usr/bin/python3
"""Defines a class Rectangle that inherits from BaseGeometry."""
class BaseGeometry:
    """Represent base geometry."""
    
    def area(self):
        """Raises an Exception since area() is not implemented in the base class."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates that the given value is a positive integer.

        Parameters:
            name (str): The name of the value being validated.
            value (int): The value to be validated.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """Represent a rectangle using BaseGeometry."""
    
    def __init__(self, width, height):
        """
        Initializes a Rectangle object with the given width and height.

        Parameters:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.

        Raises:
            TypeError: If width or height is not an integer.
            ValueError: If width or height is less than or equal to 0.
        """
        self.__width = width
        self.__height = height
        self.integer_validator("width", self.__width)
        self.integer_validator("height", self.__height)

    def area(self):
        """
        Calculates and returns the area of the rectangle.

        Returns:
            int: The area of the rectangle (width * height).
        """
        return self.__width * self.__height

class Square(Rectangle):
    """Represent a Square using Rectangle."""
    def __init__(self, size):
        """
        Initializes a Square object with the given size.

        Parameters:
            size (int): The size of the square.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than or equal to 0.
        """
        super().__init__(size, size)

    def area(self):
        """
        Calculates and returns the area of the square.

        Returns:
            int: The area of the square (side * side).
        """
        return self.__width * self.__width

    def __str__(self):
        """
        Returns a string representation of the Square.

        Returns:
            str: A formatted string with the square description [Square] <size>/<size>.
        """
        return f"[Square] {self.__width}/{self.__height}"