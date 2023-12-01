#!/usr/bin/python3

from calculator_1 import add, sub, mul, div
from sys import argv, exit

if __name__ == "__main__":

    operators = "+-*/"

    if len(argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    if argv[2] not in operators:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

    op = argv[2]
    a = int(argv[1])
    b = int(argv[3])

    if op == "+":
        print(f"{a:d} + {b:d} = {add(a, b):d}")
    elif op == "-":
        print(f"{a:d} - {b:d} = {sub(a, b):d}")
    elif op == "*":
        print(f"{a:d} * {b:d} = {mul(a, b):d}")
    else:
        print(f"{a:d} / {b:d} = {div(a, b):d}")
