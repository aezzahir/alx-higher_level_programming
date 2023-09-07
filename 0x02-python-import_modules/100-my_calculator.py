#!/usr/bin/python3
if __name__ == "__main__":
    from sys import exit, argv
    from calculator_1 import add, sub, mul, div
    operators = {"+": add, "-": sub, "*": mul, "/": div}
    if len(argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    else:
        operator = argv[2]
        if operator not in operators.keys():
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
        else:
            a = int(argv[1])
            b = int(argv[3])
            result = operators[operator](a, b)
            print("{} {} {} = {}".format(a, operator, b, result))
            exit(0)
