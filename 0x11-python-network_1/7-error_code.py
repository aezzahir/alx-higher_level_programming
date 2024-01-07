#!/usr/bin/python3
"""
7. Error code #1
"""

if __name__ == "__main__":
    import requests
    import sys
    url = sys.argv[1]
    r = requests.get(url)
    if r.status_code >= 400:
        print("Error code:", r.status_code)
    else:
        print(r.text)
