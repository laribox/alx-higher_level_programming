#!/usr/bin/python3
"""Defines a peak-finding algorithm."""


import urllib.request

# Fetch the content from the URL
with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as response:
    res = response.read()

# Print details about the response
print(
    "Body response:\n"
    "\t- type: {}\n"
    "\t- content: {}\n"
    "\t- utf8 content: {}".format(type(res), res, res.decode("utf-8"))
)
