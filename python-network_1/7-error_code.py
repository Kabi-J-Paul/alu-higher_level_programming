#!/usr/bin/python3
"""Displays a response body, or the status code when it is 400 or more."""
import requests
import sys


if __name__ == "__main__":
    response = requests.get(sys.argv[1])
    if response.status_code >= 400:
        print("Error code: {}".format(response.status_code))
    else:
        print(response.text)
