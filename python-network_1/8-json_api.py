#!/usr/bin/python3
"""This is my doc"""

import requests
import sys


def main(q="", url="http://0.0.0.0:5000/search_user"):
    try:
        q = sys.argv[1]
    except IndexError:
        pass
    data = {"q": q}
    req = requests.post(url=url, data=data)

    try:
        req_json = req.json()

    except ValueError:
        print("Not a valid JSON")
    else:
        if not req_json:
            print('No result')
        else:
            print(f'[{req_json['id']}] {req_json['name']}')


if __name__ == "__main__":
    main()
