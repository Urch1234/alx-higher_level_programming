#!/usr/bin/python3
"""Fetches https://alx-intranet.hbtn.io/status."""
import urllib.request


if __name__ = "__main__":
    request = urllib.request.Request("https://alx-intranet.htbn.io/status")
    with urllib.request.urlopen(request) as f:
        body = f.read()
        print("Body f:")
        print("\t- type: {}".format(type(body)))
        print("\t- content: {}".format(f))
        print("\t- utf8 content: {}".format(body.decode("utf-8")))
