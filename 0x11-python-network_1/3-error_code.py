#!/usr/bin/python3

"""
This script  takes in a URL, sends a request to the URL
and displays the body of the response
"""

if __name__ == "__main__":
    import urllib.request
    import urllib.error
    import sys
    url = sys.argv[1]
    try:
        with urllib.request.urlopen(url) as response:
            response_body = response.read().decode("utf-8")
            print(response_body)
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
