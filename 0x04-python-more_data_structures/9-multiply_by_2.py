#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    another = {}
    for key, value in a_dictionary.items():
        another.update({key: (value * 2)})
    return another
