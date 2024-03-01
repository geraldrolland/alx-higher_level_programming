#!/bin/bash
#This script takes in a URL, sends a GET request to the URL, and displays the body of the response
url=$1; [[ $(curl -s -L -X GET -o temp_body.txt -w "%{http_code}" "$url") -eq 200 ]] && cat temp_body.txt; rm -f temp_body.txt
