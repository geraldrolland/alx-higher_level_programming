#!/usr/bin/python3

"""
This script takes in a URL, sends a request to the URL
and displays the body of the response.
"""

if __name__ == "__main__":
    import requests
    import sys
    url = sys.argv[1]
    response = requests.get(url)
    if response.status_code < 400:
        print(response.content.decode("utf-8"))
    else:
        print("Error code: {}".format(response.status_code))
