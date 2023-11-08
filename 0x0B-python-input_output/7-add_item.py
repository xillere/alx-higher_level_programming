#!/usr/bin/python3
"""script: add all arguments to a Python list and save them to a file."""
import sys

if __name__ == "__main__":
    save_to_json_file = \
        __import__('5-save_to_json_file').save_to_json_file
    load_from_json_file = \
        __import__('6-load_from_json_file').load_from_json_file

    try:
        argus = load_from_json_file("add_item.json")
    except FileNotFoundError:
        argus = []
    argus.extend(sys.argv[1:])
    save_to_json_file(argus, "add_item.json")
