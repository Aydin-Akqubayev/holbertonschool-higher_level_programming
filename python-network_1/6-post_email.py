#!/usr/bin/python3
"""Practicing requests library"""


import requests
import sys

url = sys.argv[1]
email_addr = sys.argv[2]

data = {
    "email": email_addr
}

response = requests.post(url, data=data)
print(response.text)
