#!/usr/bin/python3
'''This is practice sys and with'''

import sys


a = sys.argv[1:]
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
filename = 'add_item.json'

lists = save_to_json_file(a, filename)
with open(filename, 'r') as f:
    full_list = f.read(3)
    print(full_list)
