#!/usr/bin/python3
def roman_to_int(roman_string):
    """ converts a Roman numeral to an integer."""
    romans = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    if (roman_string is None) or (type(roman_string) is not str):
        return 0
    num = len(roman_string)
    value = romans[roman_string[num-1]]
    for i in range(num - 1, 0, -1):
        current_value = romans[roman_string[i]]
        previous_value = romans[roman_string[i-1]]
        if previous_value >= current_value:
            value += previous_value
        else:
            value -= previous_value
    return value
