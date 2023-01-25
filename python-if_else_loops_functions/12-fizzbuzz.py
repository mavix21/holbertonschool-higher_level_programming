#!/usr/bin/python3


def fizzbuzz():
    i = 0
    s = ""

    while i <= 100:
        if i % 15 == 0:
            s = "FizzBuzz"
        elif i % 3 == 0:
            s = "Fizz"
        elif i % 5 == 0:
            s = "Buzz"
        else:
            s = i
        print("{}".format(s), end=" ")
        i += 1
