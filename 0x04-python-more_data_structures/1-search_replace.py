#!/usr/bin/python3

def search_replace(my_list, search, replace):
    another = []
    for element in my_list:
        if element == search:
            another.append(replace)
        else:
            another.append(element)
    return another
