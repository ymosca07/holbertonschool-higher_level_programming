#!/usr/bin/python3
"""Ceci est une description"""
import json


def save_to_json_file(my_obj, filename):
    """Ceci est une descriptin"""
    with open(filename, "w", encoding="utf-8") as file:
        this = file.write(json.dumps(my_obj))
    return this
