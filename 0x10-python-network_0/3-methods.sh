#!/bin/bash
# This script that takes in a URL and displays all HTTP methods the server
echo $(grep -i "Allow" <<< $(curl -s -L -X OPTIONS -i "$1")) | sed 's/Allow: //'
