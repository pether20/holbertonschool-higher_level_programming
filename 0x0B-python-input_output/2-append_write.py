#!/usr/bin/python3
""" task 01 read file"""


def append_write(filename="", text=""):
    """Methode write file"""
    with open(filename, 'r+', encoding="UTF8") as f:
        return f.write(text)
