#!/usr/bin/python3


def uppercase(str):
    i = 0
    for c in str:
        if ord(c) >= 97 and ord(c) <= 122:
            c = chr(ord(str[i]) - 32)
        print("{}".format(c), end="")
        i += 1

    print("")
