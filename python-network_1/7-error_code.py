#!/usr/bin/python3
"""Practicing requests library"""

import requests
import sys


def main():
    url = sys.argv[1]
    req = requests.get(url)
    if req.status_code >= 400:
        print(f"Error code: {req.status_code}")
    else:
        print(req.text)


if __name__ == "__main__":
    main()
