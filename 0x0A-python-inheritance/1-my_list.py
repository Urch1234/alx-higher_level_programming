#!/usr/bin/python3
"""Defines an inherited list class by MyList"""


class MyList(List):
    """Implements sorted printing for the built-in listclass."""

    def print_sorted(self):
        """Prints a list in soterd ascending order."""
        print(sorted(self))
