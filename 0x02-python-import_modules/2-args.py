#!/usr/bin/python3

if __name__ == "__main__":

    import sys

    num = len(sys.argv) - 1
    if num == 0:
        print("{} arguments.".format(num))
    else:
        print("{} arguments:".format(num))

    if num > 0:
        for i in range(num):
            print("{}: {}".format(i + 1, sys.argv[num + 1]))
