#!/bin/bash
# Sends a POST request with an email and a subject and displays the body
curl -s -X POST -d "email=test@gmail.com" -d "subject=I will always be here for PLD" "$1"
