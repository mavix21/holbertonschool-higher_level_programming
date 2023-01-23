#!/usr/bin/python3
import random
import math

number = random.randint(-10000, 10000)
lastDigit = int(math.fmod(number, 10))

print(f"Last digit of {number} is {lastDigit} and is ", end="")
if lastDigit > 5:
    print("greater than 5")
elif lastDigit == 0:
    print("0")
else:
    print("less than 6 and not 0")
