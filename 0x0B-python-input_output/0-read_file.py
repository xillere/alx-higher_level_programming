#!/usr/bin/python3
"""Defines a function that reads textfiles"""


def read_file(filename=""):
    """Prints contents of a utf-8 text file"""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
