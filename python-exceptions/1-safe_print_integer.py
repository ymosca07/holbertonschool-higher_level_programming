#!/usr/bin/python3

def safe_print_integer(value):

    try:
        print("{:d}".format(value))
        return True
    except ValueError:
        print("There is an error !")
        return False
