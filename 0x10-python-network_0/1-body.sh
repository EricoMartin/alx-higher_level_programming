#!/bin/bash
#Bash script that takes in a URL, sends a GET request to the URL
curl -s "$1" -X GET -L
