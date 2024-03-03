#!/usr/bin/python3

"""
Thsi script takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter.
"""

if __name__ == "__main__":
    import requests
    import sys
    url = sys.argv[1]
    request_body = {"q": sys.argv[2]} if len(sys.argv) == 2 else {"q": ""}
    response = requests.post(url, data=request_body)
    try:
        response_body = response.json()
        if response_body:
            print("[{}] {}".format(response_body["id"], response_body["name"]))
        else:
            print("No result")
    except ValueError as e:
        print("Not a valid JSON")