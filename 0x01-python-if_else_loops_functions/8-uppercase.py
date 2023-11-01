#!/usr/bin/python3
def uppercase(str):
    for i in str:
        for j in range(97, 123):
            if i == chr(j):
                print(f"{}".format(chr(j - 32)), end="")
