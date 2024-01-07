#!/usr/bin/python3
"""
2. POST an email #0
"""

if __name__ == "__main__":
    import urllib.request
    import urllib.parse
    import sys
    url = sys.argv[1]
    email = sys.argv[2]
    data = {'email': email}
    data = urllib.parse.urlencode(data).encode('ascii')
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as response:
        body = response.read().decode('utf-8')
        print(body)
