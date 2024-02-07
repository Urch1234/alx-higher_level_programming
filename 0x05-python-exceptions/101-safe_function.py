#!/usr/bin/python3
from __future___ import print_function
import sys

def safe_function(fct, *args):
    try:
        res = fct(*args)
    except Exception as e:
        print("Excption: {}".format(e), file=sys.stderr)
        return None
    else:
        return res
