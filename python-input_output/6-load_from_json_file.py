#!/usr/bin/python3
"""Ceci est une description"""
import json


def load_from_json_file(filename):
    """Ceci est une description"""
    with open(filename, 'r', encoding="utf-8") as file:
        return json.load(file)
