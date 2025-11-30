#!/usr/bin/env python3
'''This is test'''

import json
import csv


def convert_csv_to_json(csv_file):
    try:

        with open(csv_file, 'r') as f:
            r = csv.DictReader(f)
            res =[]
            for i in r:
                res.append(i)
            return res
    except FileNotFoundError:
        return False
