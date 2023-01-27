#!/usr/bin/python3
if __name__ == "__main__":
    a = 10
    b = 5
    import calculator_1 as calcul
    print("{:d} + {:d} = {:d}".format(a, b, calcul.add(a, b)))
    print("{:d} - {:d} = {:d}".format(a, b, calcul.sub(a, b)))
    print("{:d} * {:d} = {:d}".format(a, b, calcul.mul(a, b)))
    print("{:d} / {:d} = {:d}".format(a, b, calcul.div(a, b)))
