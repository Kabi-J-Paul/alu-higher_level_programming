#!/bin/bash
# Sends a GET request with the user id header and displays the body of the response
curl -s -H "X-School-User-Id: 98" "$1"
