#!/usr/bin/env python3
"""Ceci est une description"""
import csv
import json


def convert_csv_to_json(filename):
    """Ceci est une description"""
    data = []
    try:
        with open(filename, "r") as file:
            this = csv.DictReader(file)
        with open(data, "w") as data:
            json.dump(this, data)
        return True
    except FileNotFoundError:
        return False
