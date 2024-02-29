#!/usr/bin/env bash
#This script takes in a URL, sends a GET request to the URL and displays the body of the response
if [[ "$#" -eq 2 ]]; then
    url=$1
    response=$(curl -s -o temp_body.txt -w "%{http_code}" "$url")
    status_code=$(tail -n1 <<< "$response")
    
    if [[ $status_code -eq 200 ]]; then
        cat temp_body.txt
	rm temp_body.txt
    else
        rm temp_body.txt
    fi
fi
