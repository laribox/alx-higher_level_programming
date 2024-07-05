#!/usr/bin/python3
"""
Script that takes in a URL, sends a request to the URL and displays
the value of the X-Request-Id variable found in the header of the response
"""


import urllib.request
from sys import argv


url = argv[1]
with urllib.request.urlopen(url) as response:
    print(response.headers.get('X-Request-Id'))
