#!/usr/bin/python3
"""
5. Response header value #1
"""

if __name__ == "__main__":
    import requests
    import sys
    url = sys.argv[1]
    r = requests.get(url)
    Id = r.headers.get("X-Request-Id")
    print(Id)
