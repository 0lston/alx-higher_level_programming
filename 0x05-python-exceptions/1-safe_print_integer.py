#!/usr/bin/python3

def safe_print_integer(value):
    is_int = False
    try:
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError):
        return False
