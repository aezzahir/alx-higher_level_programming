#!/usr/bin/python3
"""
6. POST an email #1
"""

if __name__ == "__main__":
    import requests
    import sys
    url = sys.argv[1]
    email = sys.argv[2]
    data = {"email": email}
    r = requests.post(url, data=data)
    print(r.text)
