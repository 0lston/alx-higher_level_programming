#!/usr/bin/python3

if __name__ == "__main__":
    from sys import argv

    nbr_sum = 0
    for arg in argv[1:]:
        nbr_sum = int(arg) + nbr_sum

    print(nbr_sum)
