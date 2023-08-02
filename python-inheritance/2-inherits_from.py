#!/usr/bin/python3
"""Defines an inherited class-checking function."""

def inherits_from(obj, a_class):
    """
    Check if an object is an instance of a class that inherited (directly or indirectly) from the specified class.

    Parameters:
        obj: Any - The object to check.
        a_class: type - The class to compare the object against.

    Returns:
        bool: True if the object is an instance of a class that inherited from the specified class;
              otherwise, False.
    """
    return isinstance(obj, type) and issubclass(type(obj), a_class) and type(obj) != a_class
