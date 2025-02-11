#!/usr/bin/env python3
"""Ceci est une description"""
import json


def serialize_and_save_to_file(data, filename):
    """Ceci est une description"""
    with open(filename, "w") as file:
        json.dump(data, file)
    return filename

def load_and_deserialize(filename):
    """Ceci est une description"""
    with open(filename, "r") as file:
        data = json.load(file)
    return data
