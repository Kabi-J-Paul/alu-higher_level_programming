#!/usr/bin/python3
"""Sends a POST request to a search API and displays the matching user."""
import requests
import sys


if __name__ == "__main__":
    q = sys.argv[1] if len(sys.argv) > 1 else ""
    url = 'http://0.0.0.0:5000/search_user'
    response = requests.post(url, data={'q': q})
    try:
        result = response.json()
        if result:
            print("[{}] {}".format(result.get('id'), result.get('name')))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
