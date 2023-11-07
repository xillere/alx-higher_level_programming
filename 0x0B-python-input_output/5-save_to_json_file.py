#!/usr/bin/python3
"""json writing to file function."""
import json


def save_to_json_file(my_obj, filename):
    """Writes object to a text file using JSON rep"""
    with open(filename, "w") as f:
        json.dump(my_obj, f)
