#!/usr/bin/python3

def roman_to_int(roman_string):
    """
    Turning roman numeral into integer equivlaent
    parameters:
    roman_string (str): roman numeral string
    returns:
    int: integer equivalent of roman numeral    
    """
    roman_numeral_dict = {"I" : 1, "V" : 5, "X" : 10, "L" : 50, "C" : 100, "D" : 500, "M" : 1000}
    result = 0
    for i in range(len(roman_string) - 1):
        if roman_numeral_dict[roman_string[i]] < roman_numeral_dict[roman_string[i + 1]]:
            result -= roman_numeral_dict[roman_string[i]]
        else:
            result += roman_numeral_dict[roman_string[i]]
    result += roman_numeral_dict[roman_string[-1]]

    return result
