#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) != str or roman_string is None:
        return 0

    roman_to_int_map = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000,
    }

    result = 0
    prev = 0
    for char in roman_string[::-1]:
        curr = roman_to_int_map[char]
        if prev > curr:
            result -= curr
        else:
            result += curr
        prev = curr

    return result
