#!/usr/bin/python3
""" task 01 read file"""


def write_file(filename="", text=""):
    """Methode write file"""
    with open(filename, 'w', encoding="UTF8") as f:
        return f.write(text)
