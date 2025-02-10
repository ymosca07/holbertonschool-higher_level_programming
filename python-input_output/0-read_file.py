#!/usr/bin/python3
"""Defines a function that reads text file"""
def read_file(filename=""):
    with open("my_file_0.txt", "r") as file:
        filename = file.read()
        print(filename)
