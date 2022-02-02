#!/usr/bin/python3
""" task 04 read file"""


def load_from_json_file(filename):
    """Methode load fron json file"""
    import json
    with open(filename, 'w', encoding="UTF8") as f:
        return json.load(f)

