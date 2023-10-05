#!/usr/bin/python3

if __name__ == "__main__":

    import sys

    num = len(sys.argv) - 1
    result = 0
    for i in range(num):
        result = result + int(sys.argv[i + 1])
    print(result)
