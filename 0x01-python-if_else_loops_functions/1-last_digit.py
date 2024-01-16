#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
NUMBER_1 = str(number)
if NUMBER_1[-1] > "5":
    print(f"Last digit of {number:d} is {NUMBER_1[-1]} ans is greater than 5")
elif NUMBER_1[-1] == "0":
    print(f"Last digit of {number:d} is {NUMBER_1[-1]} and is 0")
else:
    print(f"Last difit of {number:d} is {NUMBER_1[-1]} and is less than 5")

