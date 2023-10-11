#!/usr/bin/python3

def uniq_add(my_list=[]):
    another = []
    sum = 0
    for num in my_list:
        if num not in another:
            sum += num
            another.append(num)
    return sum
