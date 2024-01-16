#!/usr/bin/python3
"""
Generates all possible combinations of two digits without repetition.

Numbers must be separated by a comma and space, except for the
last combination. The last combination is followed
by a new line.

"""
for digit1 in range(0, 10):
    for digit2 in range(digit1 + 1, 10):
        if digit1 == 8 and digit2 == 9:
            print("{}{}".format(digit1, digit2))
        else:
            print("{}{}".format(digit1, digit2), end=", ")
