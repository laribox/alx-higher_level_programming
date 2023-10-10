#!/usr/bin/python3
"""Reads a text file"""


def read_file(filename=""):
    """reads a file content"""
    with open(filename, mode="r", encoding="utf-8") as file:
        """opens file and closes it when done"""
        f = file.readlines()

    for lines in f:
        print(lines, end="")
