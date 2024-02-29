#!/bin/bash
# This script that takes in a URL and displays all HTTP methods the server will accept.
echo $(grep -i "Allow" <<< $(curl -s -X OPTIONS -i "$1")) | tr -d "Allow: "
