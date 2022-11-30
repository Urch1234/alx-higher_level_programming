#!/usr/bin/python3
"""print the alphabet in lowersace, not followed by a new line."""

for letter in range(97, 123):
    print("{}".format(chr(letter)), end="")
