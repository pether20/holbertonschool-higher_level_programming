#!/usr/bin/python3
""" task 04 read file"""


def save_to_json_file(my_obj, filename):
    """Methode from json to string"""
    import json
    with open(filename, 'w', encoding="UTF8") as f:
        f.write(json.dumps(my_obj, indent=4))
