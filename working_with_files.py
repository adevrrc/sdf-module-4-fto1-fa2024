"""
Description: Demonstrates handling file related exceptions.
Author: Damien Altenburg
Date: 2023-10-1
Usage: python working_with_files.py
"""

from os import path

script_directory = path.dirname(path.realpath(__file__))
filename = "data.txt"
file_path = f"{script_directory}/{filename}"
data_file = None

with open(file_path) as data_file:
    for record in data_file:
        print(record)

input("Press <enter> to continue...")
