#!/usr/bin/python3
import scapy.all as scapy

import json


def serialize_and_save_to_file(data, filename):

    '''Your code here to serialize and save data to the specified file'''

    json_file = json.dumps(data)
    with open(filename, 'w') as f:
        f.write(json_file)


def load_and_deserialize(filename):

    ''' Your code here to load and deserialize data from the specified file'''

    with open(filename, 'r') as f:
        json_file = f.read()
    return json.loads(json_file)
