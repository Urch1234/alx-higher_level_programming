#!/usr/bin/python3

def uppercase(input_str):
    """ Prints the input string in uppercase followed by a new line."""
    for char in input_str:
        if 'a' <= char <= 'z':
            print(chr(ord(char) - 32), end="")
    print()
