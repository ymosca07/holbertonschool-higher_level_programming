#!/usr/bin/python3

if __name__ == "__main__":
    """ DESC """
    import sys

    result = 0

    for arg in sys.argv[1:]:
        result += int(arg)

    print(result)
