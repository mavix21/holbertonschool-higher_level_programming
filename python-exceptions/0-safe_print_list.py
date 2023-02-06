#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    i = 0
    nb_print = 0

    try:
        while i < x:
            print(my_list[i], end="")
            i += 1
        nb_print = x
    except Exception:
        nb_print = i

    print()
    return (nb_print)
