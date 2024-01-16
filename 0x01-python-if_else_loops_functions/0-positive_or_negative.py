#!/usr/bin/python3
import random
number = random.randint(-10, 10)
if number > 0:
    print(number, f"is positive")
elif number == 0:
    print(number, f"is zero")
else:
    print(number, f"is negative")
