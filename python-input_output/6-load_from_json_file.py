#!/usr/bin/python3
'''Create object from a JSON file'''

import json


def load_from_json_file(filename):

    '''Practice json file'''

    with open(filename, 'r') as f:
        json_text = json.loads(f.read())
        return json_text
