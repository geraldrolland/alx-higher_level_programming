#!/usr/bin/python3
def uppercase(str):
    for i in str:
        for j in range(97, 123):
            if i == chr(j):
                print("{}".format(chr(j - 32)), end="")
		break
	    if j == 122:
	        print(i, end="")
		break
	    continue
