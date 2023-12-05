#!/usr/bin/python3

def no_c(my_string):
    my_list = [char for char in my_string if char.lower() != 'c']
    return "".join(my_list)
