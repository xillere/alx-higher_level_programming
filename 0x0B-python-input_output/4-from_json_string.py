#!/usr/bin/python3
"""JSON-to-object function."""
import json


def from_json_string(my_str):
    """Return the Python object representation of a JSON string.
        Dump makes object a str rep if json, loads reverts it
    """
    return json.loads(my_str)
