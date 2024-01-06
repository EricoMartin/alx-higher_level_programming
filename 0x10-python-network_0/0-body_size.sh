#!/bin/bash
#a Bash script that takes in a URL, sends a request to that URL
curl -s -w "%{size_download}\n" -o $1 | grep 'Content-Length' | awk '{print $2}'
