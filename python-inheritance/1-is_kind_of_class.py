#!/usr/bin/python3
"""Defines a class and inherited class-checking function."""

def is_kind_of_class(obj, a_class):
    """
    Check if an object is an instance of, or an instance of a class that inherited from, the specified class.

    Parameters:
        obj: Any - The object to check.
        a_class: type - The class to compare the object against.

    Returns:
        bool: True if the object is an instance of the specified class or any class that inherits from it;
              otherwise, False.
    """
    return isinstance(obj, a_class)
