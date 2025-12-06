#!/usr/bin/python3
"""Practice request library"""

import requests
import sys


def main():
    url = sys.argv[1]
    response = requests.get(url)
    print(response.headers['x-request-id'])


if __name__ == "__main__":
    main()
