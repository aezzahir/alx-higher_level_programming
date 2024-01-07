#!/usr/bin/python3
"""
8. Search API
"""
if __name__ == "__main__":
    import requests
    import sys
    url = 'http://0.0.0.0:5000/search_user'
    if len(sys.argv) > 1:
        letter = sys.argv[1]
    else:
        letter = ""
    data = {"q": letter}
    r = requests.post(url, data=data)
    try:
        r_json = r.json()
        if r_json:
            print("[{}] {}".format(r_json.get("id"), r_json.get("name")))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
