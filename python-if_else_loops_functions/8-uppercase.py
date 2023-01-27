#!/usr/bin/python3
def uppercase(str):
    for let in str:
        if (97 <= ord(let) <= 122):
            let = ord(let) - 32
            print("{:c}".format(let), end="")
        else:
            print("{}".format(let), end="")
