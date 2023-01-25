#!/usr/bin/python3


def print_last_digit(number):
    number *= -1 if number < 0 -1 else 1
    lastDigit = number % 10
    print("{}".format(lastDigit), end="")
    return lastDigit
