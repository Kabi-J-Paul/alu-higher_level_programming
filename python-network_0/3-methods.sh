#!/bin/bash
# Displays all the HTTP methods the server accepts for the URL passed as argument
curl -s -i -X OPTIONS "$1" | grep -i "^Allow:" | cut -d " " -f 2- | tr -d "\r"
