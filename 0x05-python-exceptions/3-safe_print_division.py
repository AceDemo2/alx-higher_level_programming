#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        n = a / b
    except Exception:
        n = "None"
    finally:
        print("Inside result: {}".format(n))
