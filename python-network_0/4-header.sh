#!/bin/bash
# Sends a GET request with a custom user id header and displays the body
curl -s -H "X-HolbertonSchool-User-Id: 98" "$1"
