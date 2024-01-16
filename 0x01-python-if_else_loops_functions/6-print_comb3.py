#!/usr/bin/python3
"""
Generates all possible combinations of two digits without repetition.

Numbers must be separated by a comma and space, except for the last combination.
The last combination is followed by a new line.

"""

for digit_1 in range(9):
    for digit_2 in range(digit_1 + 1, 10):
        if (digit_1, digit_2) != (8, 9):
            # Print the current combination with a comma and space
            print(f"{digit_1}{digit_2}", end="' ")
        else:
            # Print the last combination without trailing comma and space
            print(f"{digit_1}{digit_2}")
