#!/usr/bin/python3
""" task 00 read file"""


def read_file(filename=""):
    """Methode read file"""
    with open(filename, encoding="UTF8") as f:
        print(f.read(), end='')
