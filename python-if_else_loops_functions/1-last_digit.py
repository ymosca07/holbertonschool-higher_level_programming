#!/usr/bin/python3

import random

number = random.randint(-10000, 10000)

if number >= 0:
    number_ld = number % 10
    print(f"Last digit of {number} is {number_ld}", end=" ")
    if number_ld > 5:
        print("and is greater than 5")
    elif number_ld == 0:
        print("and is 0")
else:
    number_ld = (number * -1) % 10
    print(f"Last digit of {number} is -{number_ld}", end=" ")
    print("and is less than 6 and not 0")
