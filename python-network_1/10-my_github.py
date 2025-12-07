#!/usr/bin/python3
"""Using api key github"""

import requests
import sys


def main():
    username = sys.argv[1]
    password = sys.argv[2]
    url = "https://api.github.com/user"
    response = requests.get(url, auth=(username, password))

    try:
        data = response.json()
        print(data.get("id"))
    except ValueError:
        print("None")


if __name__ == "__main__":
    main()
