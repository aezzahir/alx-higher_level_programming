#!/bin/bash
# Check if URL is provided as an argument
if [ -z "$1" ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

# Use cURL to retrieve HTTP methods
methods=$(curl -sI -X OPTIONS "$1" | grep "Allow:" | cut -d " " -f 2-)

# Display the result
if [ -z "$methods" ]; then
    echo "Unable to retrieve HTTP methods for $1"
else
    echo "$methods"
fi
