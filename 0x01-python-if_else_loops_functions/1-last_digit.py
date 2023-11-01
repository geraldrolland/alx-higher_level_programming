#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number == 0:
    print(f"Last digit of {number:d} is {number:d} and is zero")
else:
    if number < -9:
        digit = number % -10
    elif number > 9:
        digit = number % 10
    if digit > 5:
        print(f"Last digit of {number:d} is {digit:d} and is greater than 5")
    elif digit == 0:
        print(f"Last digit of {number:d} is {digit:d} and is zero")
    elif digit < 6:
        print(f"Last digit of {number:d} is {digit:d} and is less than 6 and not 0")
