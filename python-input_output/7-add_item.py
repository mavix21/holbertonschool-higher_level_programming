#!/usr/bin/python3
"""
    This script adds all arguments to a Python list and save
    it as a JSON representation to a file
"""

import sys
import os
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

if __name__ == "__main__":
    argv = sys.argv
    file_to_save = "add_item.json"

    if os.path.exists(file_to_save):
        x = load_from_json_file(file_to_save)
    else:
        x = []

    for arg in argv[1:]:
        x.append(arg)

    save_to_json_file(x,  file_to_save)
