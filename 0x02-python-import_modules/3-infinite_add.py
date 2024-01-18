#!/usr/bin/python3

if __name__ == "__main__":
    """This Python script calculates the summation of all the
    command-line arguments passed to it and prints the result.
    """
    import sys

    total = 0
    for i in range(len(sys.argv) - 1):
        total += int(sys.argv[i + 1])
    print("{}".format(total))
