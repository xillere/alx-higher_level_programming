#!/usr/bin/python3
"""creates object from json file"""
import json


def load_from_json_file(filename):
    """create Python object from a json file."""
    with open(filename) as f:
        return json.load(f)
