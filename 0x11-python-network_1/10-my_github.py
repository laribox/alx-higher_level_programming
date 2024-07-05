#!/usr/bin/python3
"""
Python script that takes GitHub credentials
(username and personal access token)
and uses the GitHub API to display the user's id.

Requirements:
- Use Basic Authentication with a personal access token
as the password to access information (only read:user permission is needed).
- The first argument is the username.
- The second argument is the password (in this case, a personal access token).
- Use the requests and sys packages only.
- No need to check the number or type of arguments passed to the script.
"""
from sys import argv
import requests
from requests.auth import HTTPBasicAuth

if __name__ == "__main__":
    username = argv[1]
    password = argv[2]

    url = 'https://api.github.com/user'

    auth = HTTPBasicAuth(username, password)

    response = requests.get(url, auth=auth)
    print(response.json().get("id"))
