#!/usr/bin/python3
"""
Script that takes in a URL,
sends a request to the URL and displays
the value of the X-Request-Id variable
found in the header of the response
"""


import urllib.request
import sys

if __name__ == "__main__":
    """import the sys module and urllib module"""

    with urllib.request.urlopen(sys.argv[1]) as response:
        """open the url and save the response"""
        print(response.headers.get('X-Request-Id'))
