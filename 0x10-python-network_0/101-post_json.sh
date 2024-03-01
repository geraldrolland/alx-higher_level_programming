#!/bin/bash
# This script sends a JSON POST request to a URL passed as the first argument, and displays the body of the response.
echo $(curl -s -d @"$2" -X POST "$1")
