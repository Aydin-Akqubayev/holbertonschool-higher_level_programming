#!/usr/bin/python3
"""Practicing api post request new"""

import requests
import sys


def main(q="", url="http://0.0.0.0:5000/search_user"):
    try:
        q = sys.argv[1]
    except IndexError:
        pass
    data = {"q": q}

    try:
        req = requests.post(url=url, data=data)
        req_json = req.json()
        print(f'[{req_json['id']}] {req_json['name']}')
    except Exception:
        print("No result")


if __name__ == "__main__":
    main()
