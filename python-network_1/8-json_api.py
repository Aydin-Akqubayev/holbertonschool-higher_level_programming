#!/usr/bin/python3

import requests
import sys
import json


def main(q="", url="http://0.0.0.0:5000/search_user"):
    try:
        q = sys.argv[1]
    except IndexError:
        pass
    data = {"q": q}
    req = requests.post(url=url, data=data)
    req_json = req.json()
    try:
        print(f'[{req_json['id']}] {req_json['name']}')
    except Exception:
        print("No result")


if __name__ == "__main__":
    main()
