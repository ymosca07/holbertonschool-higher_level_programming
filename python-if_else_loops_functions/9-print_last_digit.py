#!/usr/bin/python3

def print_last_digit(number):
    if number >= 0:
        number_ld = number % 10
        print(number_ld, end="")
    else:
        number_ld = (number * -1) % 10
        print(number_ld, end="")
    return number_ld
