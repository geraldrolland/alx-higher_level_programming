#!/usr/bin/python3

"""
This script fetches https://alx-intranet.hbtn.io/status
"""
if __name__ == "__main__":
    import requests
    url = "https://alx-intranet.hbtn.io/status"
    response = requests.get(url)
    response_body = response.content.decode("utf-8")
    print("Body response:")
    print("\t- type: {}".format(type(response_body)))
    print("\t- content: {}".format(response_body))
