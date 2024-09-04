#!/usr/bin/env python3
def uppercase(ch):
    if ord(ch) >= 97 and ord(ch) <= 122:
        return ord(ch) - 32
    else:
        return ord(ch)

def uppercase(characters):
    result_str =""
    for ch in characters:
        result_str += "{:c}".format(uppercase(ch))
    print("{}".format(result_str))
