#!/usr/bin/python3
from urllib.request import Request, urlopen
import sys

url = sys.argv[1]
req = Request(url)
with urlopen(req) as response:
    html = response.getheader("X-Request-Id")
print(html)