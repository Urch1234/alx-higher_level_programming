#!?usr/bin/python3

def print_last_digit(number):
    """Prints the last digit of a number and return the value."""
    last_digit = abs(number) % 10
    print(last_digit)
    return last_digit
