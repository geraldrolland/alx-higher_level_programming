#!/usr/bin/python3
if __name__ == "__main__":
    import sys
j = 1
if len(sys.argv) == 1:
    print("{} arguments.".format(len(sys.argv) - 1))
elif len(sys.argv) == 2:
    print("{} argument:".format(len(sys.argv) - 1))
elif len(sys.argv) > 2:
    print("{} arguments:".format(len(sys.argv) - 1))
while j < len(sys.argv):
    print("{}: {}".format(j, sys.argv[j]))
    j = j + 1
