#!/usr/bin/python3


def uppercase(str):
    i = 0
    for c in str:
        if ord(c) >= 97 and ord(c) <= 122:
            print("{}".format(chr(ord(str[i]) - 32)), end="")
        else:
            print("{}".format(str[i]), end="")
        i += 1

    print("")
