#!/usr/bin/python3
"""Defines a function that reads text file"""
def read_file(filename=""):
    with open(filename, "r", encoding="utf-8") as file:
         print(file.read(), end="")
