#!/usr/bin/python3
from sys import stderr


def safe_function(fct, *args):
    try:
        return fct(*args)
    except Exception as i:
        stderr.write("Exception: " + str(i) + "\n")
        return None
