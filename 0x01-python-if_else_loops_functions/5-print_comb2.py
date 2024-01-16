#!/usr/bin/python3
# Print numbers from 0 to 99 with specific formatting
for i in range(100):
"""Print the current number with two digits and leading zeros
    Separate numbers by a comma and space, except for the last number
    """
    print(f"{i:02}", end=", " if i < 99 else "\n", flush=True)
