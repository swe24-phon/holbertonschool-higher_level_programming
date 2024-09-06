#!/usr/bin/python3

import sys

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("0")
    elif len(sys.argv) == 2:
        print("{}".format(int(sys.argv[1])))
    else:
        sum = 0  # Initialize sum
        for i in range(1, len(sys.argv)):
            sum += int(sys.argv[i])
        print("{}".format(sum))
        