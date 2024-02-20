#!/usr/bin/python3
"""Defines a file-appending function."""


def append_write(filename="", text=""):
    """Appeds a string  a string to the end of a UTF-8 text file.

    Args:
        filename (str): The name of the file to append to.
        text (str): the string to append to the file.
    Returns:
        The number of Character appended.
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)