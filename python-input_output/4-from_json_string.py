#!/usr/bin/python3
"""
Convert an JSON to python dictionary
"""
import json


def from_json_string(my_str):
    """Convert an JSON to python dictionary"""
    return json.load(my_str)
