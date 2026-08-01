#!/usr/bin/python3
"""Sends a POST request with an email parameter using urllib."""
import urllib.parse
import urllib.request
import sys


if __name__ == "__main__":
    data = urllib.parse.urlencode({'email': sys.argv[2]})
    data = data.encode('utf-8')
    with urllib.request.urlopen(sys.argv[1], data) as response:
        print(response.read().decode('utf-8'))
