#!/usr/bin/python3
"""
4. What's my status? #1
"""
import requests

if __name__ == "__main__":
    content = requests.get("https://alx-intranet.hbtn.io/status")
    print("Body response:")
    print("\t- type:", type(content.text))
    print("\t- content:", content.text)
