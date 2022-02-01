#!/usr/bin/python3
""" task 00 read file"""


def read_file(filename=""):
    """Metode read file"""
    with open("my_file_0.txt", encoding="UTF8") as f:
        print(f.read(), end='')
