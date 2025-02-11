#!/usr/bin/env python3
"""Ceci est une description"""
import csv
import json


def convert_csv_to_json(filename):
    """Ceci est une description"""
    try:
        with open(filename, "r", encoding="utf-8") as file:
            this = csv.DictReader(file)
            data_list = list(this)
        with open("data.json", "w", encoding="utf-8") as file:
            json.dump(data_list, file)
        return True
    except FileNotFoundError:
        return False
