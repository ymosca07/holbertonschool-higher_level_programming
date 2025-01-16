#!/usr/bin/python3
for i in range(100):
    if i == 99:
        print(i)
    elif i < 10:
        print(0, end="")
        print(i, end=", ")
    else:
        print(i, end=", ")
