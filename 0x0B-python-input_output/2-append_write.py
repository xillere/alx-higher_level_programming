#!/usr/bin/python3
"""Defines a appending function."""


def append_write(filename="", text=""):
    """Appends a string

    Args:
        filename (str): file name.
        text (str): str to append.
    Returns:
        no. of characters appended
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
