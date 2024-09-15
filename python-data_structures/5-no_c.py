#!/usr/bin/python3

def no_c(my_string):
    """Returns a string with all 'c' and 'C' characters removed from the input

          parameter:
          my_string (str): the input string
          return:
          str: the string with all 'c' and 'C' characters removed
    """
    result = ""
    for char in my_string:
        if char != 'c' and char != 'C':
            result += char
    return result
