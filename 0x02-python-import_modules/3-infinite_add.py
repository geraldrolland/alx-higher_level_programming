#!/usr/bin/python3
if __name__ == "__main__":
    import sys
sum_all = 0
i = 1
while i < len(sys.argv):
    sum_all = sum_all + int(sys.argv[i])
    i = i + 1
print(sum_all)
