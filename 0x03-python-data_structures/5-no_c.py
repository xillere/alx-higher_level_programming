#!/usr/bin/python3
def no_c(my_string):
    another = my_string.copy()
    for i in range(len(my_string)):
        if another[i] in 'Cc':
            another[i] = ''
    return another
