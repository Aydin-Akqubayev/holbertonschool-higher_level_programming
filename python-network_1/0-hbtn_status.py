#!/usr/bin/python3

from urllib.request import Request, urlopen

website_url = 'https://intranet.hbtn.io/status'
req = Request(website_url)
with urlopen(req) as response:
    html = response.read()

print("Body response:")
print(f"\t- type: {type(html)}")
print(f"\t- content: {html}")
print(f"\t- utf8 content: {html.decode()}")
