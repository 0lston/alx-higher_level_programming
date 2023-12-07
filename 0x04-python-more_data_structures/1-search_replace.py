#!/usr/bin/python3

def search_replace(my_list, search, replace):
    new_list = [replace if c == search else c for c in my_list]
    return new_list
