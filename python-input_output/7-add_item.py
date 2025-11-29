#!/usr/bin/python3
'''This is practice sys and with'''

import sys

a = sys.argv[1:]
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
filename = 'add_item.json'
try:
    elements = load_from_json_file(filename)
except Exception:
    elements = []

save_to_json_file(elements + a, filename)
