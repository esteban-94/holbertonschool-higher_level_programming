#!/usr/bin/python3
def uppercase(str):
    for let in str:
        if (97 <= ord(let) <= 122):
            let = chr(ord(let) - 32)
        print("{:s}".format(let), end="")
    print("")
