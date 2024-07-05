#!/usr/bin/python3
"""
Python script that takes in a URL,
sends a request to the URL and displays
the body of the response (decoded in utf-8).
"""


import requests

if __name__ == "__main__":
  r = requests.get('https://alx-intranet.hbtn.io/status')
  print(
    "Body response:\n"
    "\t- type: {}\n"
    "\t- content: {}".format(type(r.text), r.text)
  )
