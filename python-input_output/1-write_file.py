#!/usr/bin/python3
"""Defines write's def"""


def write_file(filename="", text=""):
    """This is a description"""
    with open(filename, "w", encoding="utf-8") as file:
        this = file.write(text)
    return this
