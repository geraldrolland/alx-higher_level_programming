#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    import calculator_1 as c
if (len(sys.argv) - 1) != 3:
    print("Usage: ./100-my_calculator.py <a> <operator> <b>")
    sys.exit(1)
elif sys.argv[2] not in "+-*/":
    print("Unknown operator. Available operators: +, -, * and /")
    sys.exit(1)
else:
    a = int(sys.argv[1])
    b = int(sys.argv[3])
    if sys.argv[2] == "+":
        print("{} + {} = {}".format(a, b, c.add(a, b)))
    elif sys.argv[2] == "-":
        print("{} + {} = {}".format(a, b, c.sub(a, b)))
    elif sys.argv[2] == "*":
        print("{} + {} = {}".format(a, b, c.mul(a, b)))
    else:
        print("{} + {} = {}".format(a, b, c.div(a, b)))
