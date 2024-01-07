#!/usr/bin/python3
"""
4. What's my status? #1
"""

if __name__ == "__main__":
    import requests
    content = requests.get("https://alx-intranet.hbtn.io/status")
    print("Body response:")
    print("\t- type:", type(content.text))
    print("\t- content:", content.text)
