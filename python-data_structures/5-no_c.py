#!/usr/bin/python3

def no_c(my_string):
    """Returns a string with all 'c' and 'C' characters removed from the input

          parameter:
          my_string (str): the input string
          return:
          str: the string with all 'c' and 'C' characters removed
    """
    return my_string.replace('c', '').replace('C', '')
