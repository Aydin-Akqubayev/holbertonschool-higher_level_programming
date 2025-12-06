#!/usr/bin/python3
"""This is example send POST request to email"""

from urllib.request import Request, urlopen
import urllib.parse
import sys

url = sys.argv[1]
mail_address = sys.argv[2]
print(url)
data = {
    "email": mail_address
}

data = urllib.parse.urlencode(data).encode('utf-8')

request = Request(url, method="POST", data=data)
with urlopen(request) as response:
    html = response.read().decode('utf-8')

    print(html)
