#!/usr/bin/python3
"""This is practice urllib libaryr handle with erro"""

from urllib.request import Request, urlopen
import urllib.error
import sys


def main():
    url = sys.argv[1]
    try:
        with urllib.request.urlopen(url) as r:
            print(r.read().decode('utf-8'))
    except urllib.error.HTTPError as e:
        print(f'Error code: {e.code}')


if __name__ == "__main__":
    main()
