#!/usr/bin/env bash
#This script that takes in a URL, sends a request to that URL
#and displays the size of the body of the response

if [[ "$#" -eq 1 ]]; then
    url=$1
    content_length=$(curl -s "$url" | wc -c)
    echo "$content_length"
fi
