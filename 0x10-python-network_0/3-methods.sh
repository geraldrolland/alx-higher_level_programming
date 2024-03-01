#!/bin/bash
# This script that takes in a URL and displays all HTTP methods the server
curl -s -L -X OPTIONS -i "$1" | grep "Allow: " | sed 's/Allow: //'
