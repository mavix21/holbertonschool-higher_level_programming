#!/usr/bin/python3
def no_c(my_string):
    new_string = ""
    i = 0

    for ch in my_string:
        if ch != 'c' and ch != 'C':
            new_string += my_string[i]
        i += 1

    return (new_string)
