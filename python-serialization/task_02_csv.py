#!/usr/bin/env python3
'''This is test'''

import json
import csv


def convert_csv_to_json(csv_file):
    try:
        with open(csv_file, "r", newline="") as f:
            r = list(csv.DictReader(f))
        with open("data.json", "w") as f:
            json.dump(r, f, indent=2)
        return True
    except Exception:
        return False
