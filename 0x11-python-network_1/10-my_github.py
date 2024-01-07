#!/usr/bin/python3
"""
9. My GitHub!
"""
import requests
import sys
from requests.auth import HTTPBasicAuth

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    auth = (username, password)
    url = "https://api.github.com/user"
    response = requests.get(url, auth=auth)
    if response.status_code == 200:
        user_data = response.json()
        print(user_data.get("id"))
    else:
        print(None)
