#!/usr/bin/python3

if __name__ == "__main__":

    from sys import argv

    args_nbr = len(argv) - 1

    if args_nbr == 1:
        print("{:d} argument:".format(args_nbr))
    else:
        print("{:d} arguments:".format(args_nbr))

    for i in range(1, args_nbr + 1):
        print("{}: {}".format(i, argv[i]))
