#!/usr/bin/python3
for i in range(1, 27):
    if (i % 2) != 0 :
        print("{:c}".format(123 - i), end="")
    else:
        print("{:c}".format(91 - i), end="")
