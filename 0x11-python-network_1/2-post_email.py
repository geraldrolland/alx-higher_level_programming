#!/usr/bin/python3

"""
This script  takes in a URL and an email, sends a POST request to the passed
URL with the email as a parameter, and displays the body of the response
"""

if __name__ == "__main__":
    import urllib.request
    import urllib.parse
    import sys
    url = sys.argv[1]
    value = {"email": sys.argv[2]}
    data = urllib.parse.urlencode(value)
    data = data.encode("ascii")
    request = urllib.request.Request(url, data)
    with urllib.request.urlopen(request) as response:
        response_body = response.read().decode("utf-8")
        print(response_body)
