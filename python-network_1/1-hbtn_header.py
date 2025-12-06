#!/usr/bin/python3
"""This is documentatoin about urllib"""


from urllib.request import Request, urlopen
import sys


def main():
    url = sys.argv[1]
    req = Request(url)
    with urlopen(req) as response:
        html = response.getheader("X-Request-Id")
    print(html)


if __name__ == '__main__':
    main()
