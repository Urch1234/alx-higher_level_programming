#!/usr/bin/python3
"""Defines a class-checking funtion."""


def is_same_class(obj, a_class):
    """Check if an object is exactly an instance of a given class.
    Args:
        obj (any): the object to check.
        a_class (type): The class to match the type of obj to.
    Return:
        If obj is exact sane as instance of a_class - True
        Otherwise - False.
    """
    if type(obj) == a_class:
        return True
    return False
